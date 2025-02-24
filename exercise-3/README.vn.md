Cho một mảng số nguyên nums có độ dài n, bạn muốn tạo một mảng ans có độ dài 2n sao cho:

ans[i] == nums[i] và
ans[i + n] == nums[i] với 0 <= i < n (chỉ số bắt đầu từ 0).
Cụ thể, ans là kết quả của việc nối hai mảng nums lại với nhau.

Trả về mảng ans.

Ví dụ 1:
Đầu vào: nums = [1,2,1]
Đầu ra: [1,2,1,1,2,1]

Giải thích: Mảng ans được tạo như sau:

ans = [nums[0], nums[1], nums[2], nums[0], nums[1], nums[2]]
ans = [1,2,1,1,2,1]
Ví dụ 2:
Đầu vào: nums = [1,3,2,1]
Đầu ra: [1,3,2,1,1,3,2,1]

Giải thích: Mảng ans được tạo như sau:

ans = [nums[0], nums[1], nums[2], nums[3], nums[0], nums[1], nums[2], nums[3]]
ans = [1,3,2,1,1,3,2,1]
Ràng buộc:
n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000
