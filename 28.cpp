#include <iostream>

using namespace std;

// Chess board dimensions
const int N = 4;

// Chess board
int board[N][N];

// Function to check if a queen can be placed at position (row, col)
bool is_safe(int row, int col) {
  // Check if there is a queen in the same column
  for (int i = 0; i < row; i++) {
    if (board[i][col]) {
      return false;
    }
  }

  // Check if there is a queen in the same diagonal (top-left to bottom-right)
  for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
    if (board[i][j]) {
      return false;
    }
  }

  // Check if there is a queen in the same diagonal (top-right to bottom-left)
  for (int i = row, j = col; i >= 0 && j < N; i--, j++) {
    if (board[i][j]) {
      return false;
    }
  }

  return true;
}

// Recursive function to generate all possible configurations for the 4-queens problem
void solve(int row) {
  // Base case: all queens have been placed
  if (row == N) {
    // Print the configuration
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        cout << board[i][j] << " ";
      }
      cout << endl;
    }
    cout << endl;
  }
  else {
    // Try placing a queen in each column of the current row
    for (int col = 0; col < N; col++) {
      // Check if it is safe to place a queen at position (row, col)
      if (is_safe(row, col)) {
        // Place the queen
        board[row][col] = 1;
        // Recursively solve the problem for the next row
        solve(row + 1);
        // Backtrack: remove the queen
        board[row][col] = 0;
      }
    }
  }
}

int main() {
  // Initialize the chess board
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      board[i][j] = 0;
    }
  }

  // Generate all possible configurations for the 4-queens problem
  solve(0);

  return 0;
}
