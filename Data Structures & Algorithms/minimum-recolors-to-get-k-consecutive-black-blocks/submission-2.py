class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0

        # Count W's in the first window
        for i in range(k):
            if blocks[i] == "W":
                count += 1

        ans = count

        # Slide the window
        for i in range(k, len(blocks)):
            # Remove the leftmost character
            if blocks[i - k] == "W":
                count -= 1

            # Add the new rightmost character
            if blocks[i] == "W":
                count += 1

            ans = min(ans, count)

        return ans