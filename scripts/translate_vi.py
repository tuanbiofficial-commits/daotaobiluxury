"""One-shot patch of lms/locale/vi.po with BILUXURY-prioritized translations.

Run once: `python3 scripts/translate_vi.py`. Idempotent — only fills empty msgstr
lines. Safe to re-run after upstream POT updates.
"""

import pathlib
import re

TRANSLATIONS = {
    # Actions
    "Save": "Lưu",
    "Cancel": "Huỷ",
    "Edit": "Sửa",
    "Delete": "Xoá",
    "Add": "Thêm",
    "New": "Mới",
    "Create": "Tạo",
    "Submit": "Gửi",
    "Update": "Cập nhật",
    "Remove": "Xoá",
    "Close": "Đóng",
    "Back": "Quay lại",
    "Next": "Tiếp theo",
    "Previous": "Trước",
    "Continue": "Tiếp tục",
    "Confirm": "Xác nhận",
    "Done": "Xong",
    "Start": "Bắt đầu",
    "Finish": "Hoàn thành",
    "Search": "Tìm kiếm",
    "Filter": "Lọc",
    "Sort": "Sắp xếp",
    "Reset": "Đặt lại",
    "Apply": "Áp dụng",
    "Copy": "Sao chép",
    "Download": "Tải xuống",
    "Upload": "Tải lên",
    "Import": "Nhập",
    "Export": "Xuất",
    "Attach": "Đính kèm",
    "View": "Xem",
    "Preview": "Xem trước",
    "Publish": "Xuất bản",
    "Unpublish": "Gỡ xuất bản",
    "Approve": "Duyệt",
    "Reject": "Từ chối",
    "Enroll": "Ghi danh",
    "Unenroll": "Huỷ ghi danh",
    "Retry": "Thử lại",
    "Refresh": "Làm mới",
    "Skip all": "Bỏ qua tất cả",
    "See all": "Xem tất cả",
    "Show more": "Xem thêm",
    "Show less": "Ẩn bớt",
    "Learn More": "Tìm hiểu thêm",
    "Get Started": "Bắt đầu ngay",
    "Log out": "Đăng xuất",
    "Log in": "Đăng nhập",
    "Login": "Đăng nhập",
    "Logout": "Đăng xuất",
    "Sign Up": "Đăng ký",
    "Sign Out": "Đăng xuất",

    # Core LMS nouns
    "Course": "Khoá học",
    "Courses": "Khoá học",
    "Lesson": "Bài học",
    "Lessons": "Bài học",
    "Chapter": "Chương",
    "Chapters": "Chương",
    "Quiz": "Bài trắc nghiệm",
    "Quizzes": "Bài trắc nghiệm",
    "Question": "Câu hỏi",
    "Questions": "Câu hỏi",
    "Assignment": "Bài tập",
    "Assignments": "Bài tập",
    "Submission": "Bài nộp",
    "Submissions": "Bài nộp",
    "Program": "Chương trình",
    "Programs": "Chương trình",
    "Batch": "Lớp",
    "Batches": "Lớp",
    "Batch Name": "Tên lớp",
    "Student": "Học viên",
    "Students": "Học viên",
    "Instructor": "Giảng viên",
    "Instructors": "Giảng viên",
    "Mentor": "Cố vấn",
    "Mentors": "Cố vấn",
    "Evaluator": "Giám khảo",
    "Evaluators": "Giám khảo",
    "Certificate": "Chứng chỉ",
    "Certificates": "Chứng chỉ",
    "Certification": "Chứng nhận",
    "Certifications": "Chứng nhận",
    "Learning": "Học tập",
    "Home": "Trang chủ",
    "Notifications": "Thông báo",
    "Profile": "Hồ sơ",
    "My Profile": "Hồ sơ của tôi",
    "Settings": "Cài đặt",
    "Statistics": "Thống kê",
    "Achievements": "Thành tích",
    "Progress": "Tiến độ",
    "Completion": "Hoàn thành",
    "Completed": "Đã hoàn thành",
    "In Progress": "Đang học",
    "Pending": "Chờ xử lý",
    "Passed": "Đạt",
    "Failed": "Không đạt",
    "Draft": "Bản nháp",
    "Published": "Đã xuất bản",
    "Active": "Đang hoạt động",
    "Inactive": "Không hoạt động",
    "Enabled": "Đã bật",
    "Disabled": "Đã tắt",
    "All": "Tất cả",
    "None": "Không",
    "Yes": "Có",
    "No": "Không",

    # Form labels
    "Name": "Tên",
    "Title": "Tiêu đề",
    "Description": "Mô tả",
    "Short Introduction": "Giới thiệu ngắn",
    "Image": "Hình ảnh",
    "Video": "Video",
    "Cover Image": "Ảnh bìa",
    "Tags": "Thẻ",
    "Category": "Danh mục",
    "Date": "Ngày",
    "Time": "Giờ",
    "Duration": "Thời lượng",
    "Start Date": "Ngày bắt đầu",
    "End Date": "Ngày kết thúc",
    "Email": "Email",
    "Username": "Tên đăng nhập",
    "Password": "Mật khẩu",
    "Full Name": "Họ và tên",
    "First Name": "Tên",
    "Last Name": "Họ",
    "Middle Name": "Tên đệm",
    "Phone": "Điện thoại",
    "Address": "Địa chỉ",
    "Country": "Quốc gia",
    "Language": "Ngôn ngữ",
    "Timezone": "Múi giờ",
    "Time Zone": "Múi giờ",
    "Status": "Trạng thái",
    "Type": "Loại",
    "Price": "Giá",
    "Amount": "Số tiền",
    "Currency": "Đơn vị tiền",
    "Role": "Vai trò",
    "Roles": "Vai trò",
    "Permission": "Quyền",
    "Permissions": "Quyền",

    # Course-specific
    "Add Course": "Thêm khoá học",
    "Add Chapter": "Thêm chương",
    "Add Lesson": "Thêm bài học",
    "Add Question": "Thêm câu hỏi",
    "Add Quiz to Video": "Thêm trắc nghiệm vào video",
    "Add a chapter": "Thêm một chương",
    "Add a lesson": "Thêm một bài học",
    "Add a Chapter": "Thêm chương",
    "Add a Lesson": "Thêm bài học",
    "Create Course": "Tạo khoá học",
    "Create your first course": "Tạo khoá học đầu tiên",
    "Add your first chapter": "Thêm chương đầu tiên",
    "Add your first lesson": "Thêm bài học đầu tiên",
    "Create your first quiz": "Tạo bài trắc nghiệm đầu tiên",
    "Create your first batch": "Tạo lớp đầu tiên",
    "Invite your team and students": "Mời đội ngũ và học viên",
    "Add students to your batch": "Thêm học viên vào lớp",
    "Add courses to your batch": "Thêm khoá vào lớp",
    "About the Course": "Giới thiệu khoá học",
    "Course Overview": "Tổng quan khoá học",
    "Course Content": "Nội dung khoá học",
    "Course Details": "Chi tiết khoá học",
    "Enroll in this Course": "Ghi danh khoá này",
    "Enroll Now": "Ghi danh ngay",
    "Enrolled": "Đã ghi danh",
    "Continue Learning": "Tiếp tục học",
    "Mark as Complete": "Đánh dấu hoàn thành",
    "Mark as Incomplete": "Đánh dấu chưa hoàn thành",
    "All Courses": "Tất cả khoá học",
    "My Courses": "Khoá của tôi",
    "Our Popular Courses": "Khoá phổ biến",
    "My Batches": "Lớp của tôi",
    "Our Upcoming Batches": "Lớp sắp khai giảng",
    "Upcoming Live Classes": "Lớp học trực tiếp sắp tới",
    "Welcome to Frappe Learning": "Chào mừng đến với BILUXURY Academy",

    # Quiz / Assignment
    "Marks": "Điểm",
    "Score": "Điểm",
    "Total Marks": "Tổng điểm",
    "Passing Percentage": "Điểm đạt (%)",
    "Attempts": "Số lần làm",
    "Result": "Kết quả",
    "Results": "Kết quả",
    "Correct": "Đúng",
    "Incorrect": "Sai",
    "Correct Answer": "Đáp án đúng",
    "Your Answer": "Câu trả lời của bạn",
    "Start Quiz": "Bắt đầu làm bài",
    "Submit Quiz": "Nộp bài",
    "Submit Assignment": "Nộp bài tập",
    "Quiz Submitted": "Đã nộp bài trắc nghiệm",
    "Assignment Submitted": "Đã nộp bài tập",
    "Mandatory": "Bắt buộc",
    "Optional": "Tuỳ chọn",
    "Retry Quiz": "Làm lại",
    "Review": "Xem lại",
    "Grade": "Chấm điểm",
    "Feedback": "Phản hồi",
    "Add a comment": "Thêm bình luận",

    # Messages / prompts
    "Are you sure?": "Bạn có chắc không?",
    "This action cannot be undone.": "Thao tác này không thể hoàn tác.",
    "Required": "Bắt buộc",
    "This field is required.": "Trường này là bắt buộc.",
    "Loading...": "Đang tải...",
    "No results found.": "Không tìm thấy kết quả.",
    "No data": "Không có dữ liệu",
    "Success": "Thành công",
    "Error": "Lỗi",
    "Warning": "Cảnh báo",
    "Info": "Thông tin",

    # Certificate
    "Certificate of Completion": "Chứng chỉ hoàn thành",
    "Awarded to": "Cấp cho",
    "Date of Completion": "Ngày hoàn thành",
    "Certificate ID": "Mã chứng chỉ",
    "Download Certificate": "Tải chứng chỉ",
    "Get Certified": "Nhận chứng chỉ",
    "View Certificate": "Xem chứng chỉ",
    "Share Certificate": "Chia sẻ chứng chỉ",

    # User management
    "Users": "Người dùng",
    "Add User": "Thêm người dùng",
    "New User": "Người dùng mới",
    "Invite User": "Mời người dùng",
    "Send Welcome Email": "Gửi email chào mừng",
    "User Category": "Loại người dùng",

    # Onboarding widget
    "Getting started": "Bắt đầu",
    "Welcome to Frappe Learning": "Chào mừng đến với BILUXURY Academy",

    # Banner
    "Welcome": "Chào mừng",
    "Hello": "Xin chào",

    # Time / date
    "Today": "Hôm nay",
    "Yesterday": "Hôm qua",
    "Tomorrow": "Ngày mai",
    "This Week": "Tuần này",
    "This Month": "Tháng này",
    "This Year": "Năm nay",
    "Last Updated": "Cập nhật lần cuối",
    "Created": "Đã tạo",
    "Updated": "Đã cập nhật",

    # Nav / sidebar specific (already translated via frontend too)
    "More": "Thêm",

    # Extra student-facing
    "Achievements": "Thành tích",
    "Streak": "Chuỗi ngày học",
    "Days": "Ngày",
    "Minutes": "Phút",
    "Hours": "Giờ",
    "per week": "mỗi tuần",
    "This class has ended": "Lớp học đã kết thúc",
    "Ended": "Đã kết thúc",
    "Join": "Tham gia",
    "Jobs": "Cơ hội nghề nghiệp",
    "Programming Exercises": "Bài thực hành lập trình",

    # Course settings / dashboard page
    "Overview": "Tổng quan",
    "Dashboard": "Bảng điều khiển",
    "Details": "Chi tiết",
    "Tags": "Thẻ",
    "Color": "Màu",
    "Select a fallback color for the course card when no image is set.": "Chọn màu hiển thị mặc định khi khoá chưa có ảnh bìa.",
    "Publishing Settings": "Cài đặt xuất bản",
    "Make the course visible to all users.": "Cho phép mọi người dùng xem khoá học.",
    "Upcoming": "Sắp ra mắt",
    "Mark the course as upcoming but not yet open for enrollment.": "Đánh dấu khoá sắp ra mắt nhưng chưa mở ghi danh.",
    "Published On": "Ngày xuất bản",
    "Featured": "Nổi bật",
    "Highlight the course on the homepage.": "Hiển thị khoá này nổi bật trên trang chủ.",
    "Allow Self Enrollment": "Cho phép tự ghi danh",
    "Allow users to enroll in this course on their own.": "Cho phép học viên tự ghi danh vào khoá mà không cần mời.",
    "About the Course": "Giới thiệu khoá học",
    "Preview Video": "Video giới thiệu",
    "Chapters": "Chương học",
    "Lessons": "Bài học",
    "Add a keyword and press enter": "Nhập từ khoá và bấm Enter",
    "Add a Chapter": "Thêm chương",
    "Add a Lesson": "Thêm bài học",
    "Welcome to Frappe Learning": "Chào mừng đến với BILUXURY Academy",

    # Onboarding widget
    "Getting started": "Bắt đầu",
    "Reset all": "Đặt lại tất cả",
    "Skip all": "Bỏ qua tất cả",
    "Help centre": "Trung tâm hỗ trợ",
    "Help Center": "Trung tâm hỗ trợ",
    "Help center": "Trung tâm hỗ trợ",
    "steps completed": "bước hoàn thành",
    "step completed": "bước hoàn thành",

    # Generic UI copy
    "Information": "Thông tin",
    "Are you sure you want to delete this?": "Bạn có chắc muốn xoá không?",
    "No items": "Không có mục nào",
    "No records found": "Không tìm thấy dữ liệu",
    "Select": "Chọn",
    "Select File": "Chọn tệp",
    "Choose file": "Chọn tệp",
    "Drop files here to upload": "Kéo thả tệp vào đây để tải lên",
    "Uploading...": "Đang tải lên...",
    "File uploaded": "Tải lên thành công",
    "All rights reserved.": "Mọi quyền được bảo lưu.",

    # Permission / auth
    "Access Denied": "Truy cập bị từ chối",
    "You don't have permission": "Bạn không có quyền",
    "Not Permitted": "Không được phép",
    "Login Required": "Yêu cầu đăng nhập",

    # Common statuses
    "Open": "Mở",
    "Closed": "Đóng",
    "Scheduled": "Đã lên lịch",
    "Cancelled": "Đã huỷ",
    "Expired": "Đã hết hạn",

    # Batch-specific
    "Batch Title": "Tên lớp",
    "Seat Count": "Số chỗ",
    "Start Time": "Giờ bắt đầu",
    "End Time": "Giờ kết thúc",
    "Medium": "Hình thức",
    "Online": "Trực tuyến",
    "Offline": "Trực tiếp",
    "Hybrid": "Kết hợp",
    "Live Class": "Lớp học trực tiếp",
    "Live Classes": "Lớp học trực tiếp",

    # Lesson editor
    "Add a quiz to your lesson": "Thêm bài trắc nghiệm vào bài học",
    "Add a programming exercise to your lesson": "Thêm bài thực hành lập trình vào bài học",
    "Body": "Nội dung",
    "Content": "Nội dung",
    "Chapter Title": "Tên chương",
    "Lesson Title": "Tên bài học",
    "Include in Preview": "Cho phép xem thử",
    "Paid Lesson": "Bài học trả phí",

    # Quiz form
    "Quiz Title": "Tên bài trắc nghiệm",
    "Max Attempts": "Số lần làm tối đa",
    "Make the Quiz a Practice": "Đặt làm bài luyện tập",
    "Shuffle Questions": "Trộn câu hỏi",

    # Payment / pricing (even if unused by BILUXURY)
    "Free": "Miễn phí",
    "Paid": "Trả phí",
    "Amount Paid": "Số tiền đã thanh toán",

    # Date/time extra
    "Jan": "Th1", "Feb": "Th2", "Mar": "Th3", "Apr": "Th4",
    "May": "Th5", "Jun": "Th6", "Jul": "Th7", "Aug": "Th8",
    "Sep": "Th9", "Oct": "Th10", "Nov": "Th11", "Dec": "Th12",
    "Monday": "Thứ Hai", "Tuesday": "Thứ Ba", "Wednesday": "Thứ Tư",
    "Thursday": "Thứ Năm", "Friday": "Thứ Sáu", "Saturday": "Thứ Bảy",
    "Sunday": "Chủ Nhật",
}


def patch_po(path: pathlib.Path, translations: dict) -> int:
    text = path.read_text(encoding="utf-8")
    # Match blocks of: msgid "..." \n (optional continuation "...") \n msgstr ""
    # For simplicity, handle single-line msgid/msgstr pairs (most common).
    pattern = re.compile(r'^msgid "(?P<id>(?:[^"\\]|\\.)*)"\nmsgstr ""$', re.MULTILINE)
    filled = 0

    def repl(match):
        nonlocal filled
        msgid = match.group("id")
        # Unescape basic \" and \\ inside msgid for dict lookup
        key = msgid.replace('\\"', '"').replace("\\\\", "\\")
        if key in translations:
            val = translations[key].replace("\\", "\\\\").replace('"', '\\"')
            filled += 1
            return f'msgid "{msgid}"\nmsgstr "{val}"'
        return match.group(0)

    new_text = pattern.sub(repl, text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return filled


if __name__ == "__main__":
    po_path = pathlib.Path(__file__).parent.parent / "lms" / "locale" / "vi.po"
    n = patch_po(po_path, TRANSLATIONS)
    print(f"Filled {n} Vietnamese translations in {po_path.name}")
