#include <iostream>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

#define UP 0
#define DOWN 1
#define LEFT 2
#define RIGHT 3

struct PuzzleState {
    int board[5][5];
    int emptyY;
    int emptyX;
    std::vector<int> moves; // 이동 경로 저장
};

bool isValidMove(int y, int x) {
    return y >= 0 && y < 5 && x >= 0 && x < 5;
}

std::vector<PuzzleState> getNeighbors(PuzzleState& state) {
    static const int dy[4] = {-1, 1, 0, 0}; // UP, DOWN
    static const int dx[4] = {0, 0, -1, 1}; // LEFT, RIGHT
    std::vector<PuzzleState> neighbors;

    for (int dir = 0; dir < 4; ++dir) {
        int newY = state.emptyY + dy[dir];
        int newX = state.emptyX + dx[dir];
        if (isValidMove(newY, newX)) {
            PuzzleState newState = state;
            std::swap(newState.board[state.emptyY][state.emptyX], newState.board[newY][newX]);
            newState.emptyY = newY;
            newState.emptyX = newX;
            newState.moves.push_back(dir);
            neighbors.push_back(newState);
        }
    }
    return neighbors;
}

std::vector<int> moveNumberToEmpty(int board[5][5], int targetY, int targetX) {
    std::queue<PuzzleState> queue;
    std::map<std::vector<int>, bool> visited;
    std::vector<int> initialBoardVec;

    PuzzleState initialState;
    memcpy(initialState.board, board, sizeof(initialState.board));
    for (int y = 0; y < 5; y++) {
        for (int x = 0; x < 5; x++) {
            initialBoardVec.push_back(board[y][x]);
            if (board[y][x] == 0) {
                initialState.emptyY = y;
                initialState.emptyX = x;
            }
        }
    }

    visited[initialBoardVec] = true;
    queue.push(initialState);

    while (!queue.empty()) {
        PuzzleState currentState = queue.front();
        queue.pop();

        if (currentState.emptyY == targetY && currentState.emptyX == targetX) {
            return currentState.moves; // 목표 도달시 경로 반환
        }

        std::vector<PuzzleState> neighbors = getNeighbors(currentState);
        for (PuzzleState& neighbor : neighbors) {
            std::vector<int> boardVec;
            for (int y = 0; y < 5; y++) {
                for (int x = 0; x < 5; x++) {
                    boardVec.push_back(neighbor.board[y][x]);
                }
            }

            if (!visited[boardVec]) {
                visited[boardVec] = true;
                queue.push(neighbor);
            }
        }
    }

    return std::vector<int>(); // 경로가 없을 경우 빈 벡터 반환
}

int main() {
    int board[5][5] = {
        {1, 2, 3, 4, 5},
        {6, 7, 8, 9, 10},
        {11, 12, 0, 13, 14},
        {15, 16, 17, 18, 19},
        {20, 21, 22, 23, 24}
    };
    int targetY = 2, targetX = 2; // 원하는 빈 칸 위치
    std::vector<int> moves = moveNumberToEmpty(board, targetY, targetX);

    for (int move : moves) {
        std::cout << "Move: " << move << std::endl;
    }
    for (auto i : board)
    {

        std::cout << i << std::endl;
    }

    return 0;
}
