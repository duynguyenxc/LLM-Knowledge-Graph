Edited Pydantic_Leiden.txt
Edited implementation_plan.md

Tôi đã ghi nhận toàn bộ các góc nhìn cực kỳ sâu sắc và mang tiêu chuẩn học thuật khắt khe của bạn. Dưới góc nhìn của một nhà nghiên cứu chuyên nghiệp để chuẩn bị cho RRE 2026, tôi đã **cập nhật lại Implementation Plan** để phân tích rạch ròi 3 điểm cốt lõi bạn vừa nhấn mạnh.

Dưới đây là tóm tắt chiến lược đã được tôi đưa vào bản thiết kế:

### 1. Kiến trúc Multi-Agent (Các tầng Layer & Thuật toán)
Chúng ta sẽ không dùng một "AI thông minh" để làm mọi thứ (như ChatGPT), mà sẽ dùng **LangGraph** để xây dựng mô hình Finite State Machine (Cỗ máy trạng thái hữu hạn), chia nhỏ thành các hạt nhân:
*   **Layer 1 (Điều phối - Orchestrator):** StateGraph định tuyến luồng dữ liệu (Routing). Nó sẽ quyết định quy trình đi từ Tìm kiếm -> Trích xuất -> Nếu báo lỗi thì quay vòng lại (Cyclic FSM).
*   **Layer 2 (Các Agents chuyên biệt):** Đây chính là sức mạnh của Multi-Agent. Ta sẽ có riêng: 
    *   *Screening Agent* (Giỏi sàng lọc Inclusion/Exclusion)
    *   *CMOC Extraction Agent* (Giỏi bóc tách ngữ nghĩa)
    *   *Contradiction Agent* (Chuyên viên phản biện: Đọc LKG để tìm ra những đoạn bằng chứng đá nhau giữa các tệp PDF).
    *   *Cross-Study Synthesis Agent* (Chuyên viên tóm tắt cộng đồng Leiden).
*   **Layer 3 (Quản trị HITL):** Lớp vòng ngoài nơi con người đóng vai trò chốt chặn Master Control.

### 2. Thiết kế Schema / Ontology (Nền móng của Knowledge Graph)
Như bạn đã nói, thiết kế Schema là sự sống còn của dự án.
*   **Chiến lược:** Ta áp dụng **Strict Ontology Mapping**. Các Pydantic Schema trong Python sẽ được tôi code "cứng" (Hard-code) hoàn toàn dựa trên mạng lưới 47 Entities (`E01`-`E47`) và các Relationships (`LEADS_TO`, `ENABLES`, `TRIGGERS`) nằm trong tài liệu *Richmond-KG-Specification.pdf* mà bạn đã từng phân tích. 
*   **Hiệu quả:** AI không có cửa tự "phóng tác". Nó bắt buộc phải bám chặt theo Ontology của Richmond.

### 3. Tối ưu Prompt (Prompt Engineering Strategy)
Prompt không chỉ là nhập văn bản bình thường. Để tối ưu chất lượng:
*   **Từ chối Zero-shot AI:** Chúng ta tuyệt đối không dùng Zero-shot (Bảo AI tự làm mà không có ví dụ). Ta sẽ dùng **Dynamic Few-Shot Prompting**. Mã nguồn sẽ tự động lấy các ví dụ gốc từ Richmond (2020) chèn vào Prompt để mớm cho AI biết thế nào là "khái niệm" đúng.
*   **GraphRAG Prompt Tuning:** Ta sẽ chạy thuật toán tự động Tuning Prompt chuyên biệt cho giáo dục y khoa lâm sàng chứ không để prompt mặc định của Microsoft Graph. Mọi Persona (Vai trò) của Prompt đều sẽ mang tư duy của "Realist Evaluator" (người đánh giá thực tế).

Tất cả đã được bổ sung chi tiết vào trong file `implementation_plan.md` ở trên. Bạn hãy đọc lướt qua xem các luồng kiến trúc (Architecture) cũng như thiết kế Ontology đã đi đúng mạch của nghiên cứu chưa. 

**Nếu mọi thứ đã hoàn hảo tạo thành một quy chuẩn sắc bén, hãy báo "Duyệt" (Approve) nhé. Tới lúc đó, tôi sẽ chính thức bắt tay vào việc khởi tạo Folder và viết những dòng code kiến trúc nền tảng đầu tiên!**