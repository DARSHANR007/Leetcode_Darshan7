class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        moves = 0
        seats.sort()
        students.sort()
        for s in range(len(students)):
            moves += abs(students[s]-seats[s])
        return moves