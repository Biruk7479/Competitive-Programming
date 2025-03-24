class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # Sort by start day
        available = 0
        last_end = 0  # Track the last occupied day
                    
        for start, end in meetings:
            if start > last_end + 1:
                available += (start - last_end - 1)  # Count gap days
            last_end = max(last_end, end)  # Merge overlapping meetings
                # Consider the free days after the last meeting
        if last_end < days:
            available += (days - last_end)
        return available