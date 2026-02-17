class Solution:
 def readBinaryWatch(self , turnedOn: int):
    result = []
    for h in range(12):  # hours: 0–11
        for m in range(60):  # minutes: 0–59
            # Count LEDs turned on in hour + minute
            if (bin(h).count("1") + bin(m).count("1")) == turnedOn:
                # Format: hour without leading zero, minute with 2 digits
                result.append(f"{h}:{m:02d}")
    return result
 
# Example Usage:
sol = Solution()
print(sol.readBinaryWatch(1))
