class ShogiBoard:
  def __init__(self):
      self.board = [
          ['l', 'n', 's', 'g', 'k', 'g', 's', 'n', 'l'],
          ['.', 'r', '.', '.', '.', '.', '.', 'b', '.'],
          ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
          ['.', 'B', '.', '.', '.', '.', '.', 'R', '.'],
          ['L', 'N', 'S', 'G', 'K', 'G', 'S', 'N', 'L']
      ]

  def display_board(self):
      for row in self.board:
          print(' '.join(row))

  def move_piece(self, start_row, start_col, end_row, end_col):
      if self.is_valid_move(start_row, start_col, end_row, end_col):
          piece = self.board[start_row][start_col]
          self.board[start_row][start_col] = '.'  # Limpa a posição inicial
          self.board[end_row][end_col] = piece  # Move a peça para a nova posição
          self.display_board()  # Imprime o tabuleiro atualizado após o movimento
      else:
          print("Movimento inválido!")

  def is_valid_move(self, start_row, start_col, end_row, end_col):
      piece = self.board[start_row][start_col]
      target_piece = self.board[end_row][end_col]

      # Verificar se as coordenadas estão dentro do tabuleiro
      if not (0 <= start_row < 9 and 0 <= start_col < 9 and 0 <= end_row < 9 and 0 <= end_col < 9):
          return False

      # Verificar se a peça é movida para a mesma posição
      if start_row == end_row and start_col == end_col:
          return False

      # Implementar lógica específica de validação para cada tipo de peça
      if piece == 'p':  # Movimento dos peões
          if start_col == end_col:  # Movimento para frente
              if start_row - 1 == end_row:
                  return True
          elif abs(start_col - end_col) == 1 and start_row - 1 == end_row:  # Movimento de captura diagonal
              return True
      elif piece == 'l':  # Movimento do lanceiro
          if start_col == end_col:  # Movimento na mesma coluna
              if start_row > end_row:  # Movimento para frente
                  for row in range(start_row - 1, end_row, -1):
                      if self.board[row][start_col] != '.':  # Verifica se há alguma peça no caminho
                          return False  # Não pode pular sobre outras peças
                  return True
      # Adicionar lógica para outros tipos de peça...

      # Caso padrão: movimento válido se a célula de destino estiver vazia
      return target_piece == '.'


if __name__ == "__main__":
  shogi_game = ShogiBoard()
  shogi_game.display_board()
  print("Movendo um peão...\n\n")
  shogi_game.move_piece(2, 1, 3, 1)  # Movimento válido de um peão para frente
  print("\n\nMovendo outro peão...")
  shogi_game.move_piece(2, 2, 3, 2)  # Movimento válido de outro peão para frente
  print("\n\nMovendo outro peão...")
  shogi_game.move_piece(2, 0, 3, 0)  # Movimento válido de outro peão para frente
  print("\n\nMovendo o lanceiro...")
  shogi_game.move_piece(0, 0, 3, 0)  # Movimento inválido do lanceiro tentando pular um peão
