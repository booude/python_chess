import pygame as p
from const import *
from board import Board
from dragger import Dragger


class Game:
    def __init__(self):
        self.next_player = "w"
        self.hovered_sqr = None
        self.board = Board()
        self.dragger = Dragger()

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                p.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = p.image.load(piece.texture)
                        img_center = (
                            col * SQSIZE + SQSIZE // 2,
                            row * SQSIZE + SQSIZE // 2,
                        )
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece

            for move in piece.moves:
                color = (
                    "#C4C4C4"
                    if (move.final.row + move.final.col) % 2 == 0
                    else "#A4A4A4"
                )
                rect = (
                    move.final.col * SQSIZE,
                    move.final.row * SQSIZE,
                    SQSIZE,
                    SQSIZE,
                )
                p.draw.rect(surface, color, rect)

    def show_last_move(self, surface):
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                color = (244,247,116) if (pos.row + pos.col) % 2 == 0 else (172,195,51)
                rect = (
                    pos.col * SQSIZE,
                    pos.row * SQSIZE,
                    SQSIZE,
                    SQSIZE,
                )
                p.draw.rect(surface, color, rect)

    def show_hover(self, surface):
        if self.hovered_sqr:
            color = (180,180,180)
            rect = (
                self.hovered_sqr.col * SQSIZE,
                self.hovered_sqr.row * SQSIZE,
                SQSIZE,
                SQSIZE)
            p.draw.rect(surface, color, rect, width=3)

    def next_turn(self):
        self.next_player = "w" if self.next_player == "b" else "b"

    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]
