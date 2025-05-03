-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th12 20, 2024 lúc 05:46 AM
-- Phiên bản máy phục vụ: 10.4.27-MariaDB
-- Phiên bản PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `quanlysinhvien`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `buoihoc`
--

CREATE TABLE `buoihoc` (
  `mabuoihoc` varchar(10) NOT NULL,
  `giobatdau` text NOT NULL,
  `gioketthuc` text NOT NULL,
  `ngay` date NOT NULL,
  `malop` varchar(10) DEFAULT NULL,
  `magiangvien` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `buoihoc`
--

INSERT INTO `buoihoc` (`mabuoihoc`, `giobatdau`, `gioketthuc`, `ngay`, `malop`, `magiangvien`) VALUES
('BH001', '08:00:00', '10:00:01', '2024-12-20', 'L001', 'GV001'),
('BH002', '09:00:00', '10:00:01', '2024-12-21', 'L003', 'GV005'),
('BH003', '10:00:00', '11:30:00', '2024-12-20', 'L005', 'GV006'),
('BH004', '20:00:00', '21:00:00', '2024-12-20', 'L002', 'GV008');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chucnang`
--

CREATE TABLE `chucnang` (
  `machucnang` varchar(10) NOT NULL,
  `tenchucnang` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `chucnang`
--

INSERT INTO `chucnang` (`machucnang`, `tenchucnang`) VALUES
('CN001', 'Quản lý sinh viên'),
('CN002', 'Điểm danh'),
('CN003', 'Quản lý giảng viên'),
('CN004', 'Quản lý buổi học'),
('CN005', 'Nhận diện khuôn mặt'),
('CN006', 'Thống kê'),
('CN007', 'Quản lý tài khoản'),
('CN008', 'Thay đổi mật khẩu'),
('CN009', 'Điểm danh sự kiện');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `diemdanh`
--

CREATE TABLE `diemdanh` (
  `madiemdanh` varchar(20) NOT NULL,
  `masinhvien` varchar(20) DEFAULT NULL,
  `giovao` varchar(255) DEFAULT NULL,
  `giora` varchar(255) DEFAULT NULL,
  `mabuoihoc` varchar(20) DEFAULT NULL,
  `hinhanh` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `diemdanh`
--

INSERT INTO `diemdanh` (`madiemdanh`, `masinhvien`, `giovao`, `giora`, `mabuoihoc`, `hinhanh`) VALUES
('DD003', 'SV3121411206', '00:00:00', '00:00:00', 'BH001', ''),
('DD004', 'SV3121411206', '06:46:11', NULL, 'BH001', ''),
('DD005', 'SV3121411206', '06:54:18', '06:54:37', 'BH002', ''),
('DD006', 'SV3121411206', '06:54:18', '06:54:37', 'BH002', ''),
('DD007', 'SV3121330069', '08:13:58', '08:14:54', 'BH002', ''),
('DD008', 'SV3121330069', '00:00:00', '00:00:00', 'BH002', ''),
('DD009', 'SV3121330069', '08:37:57', '08:38:20', 'BH001', ''),
('DD010', 'SV3121330069', '08:37:57', '08:38:20', 'BH001', ''),
('DD011', 'SV3121350016', '00:00:00', '00:00:00', 'BH001', ''),
('DD012', 'SV3121350016', '09:32:48', '09:33:36', 'BH001', ''),
('DD013', 'SV3121350016', '09:32:48', '09:33:36', 'BH001', ''),
('DD015', 'SV3121350016', '09:32:48', '09:33:36', 'BH001', ''),
('DD016', 'SV3121350016', '09:32:48', '09:33:36', 'BH001', ''),
('DD017', 'SV3121411206', '10:26:50', '11:16:36', 'BH003', ''),
('DD018', 'SV3121411206', '00:00:00', '11:16:36', 'BH003', '');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `giangvien`
--

CREATE TABLE `giangvien` (
  `magiangvien` varchar(10) NOT NULL,
  `hoten` varchar(255) NOT NULL,
  `sodienthoai` varchar(15) DEFAULT NULL,
  `mataikhoan` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `giangvien`
--

INSERT INTO `giangvien` (`magiangvien`, `hoten`, `sodienthoai`, `mataikhoan`) VALUES
('GV001', 'Nguyễn Văn A', '0987654321', 'TK001'),
('GV002', 'Trần Thị B', '391234562', 'TK004'),
('GV003', 'Lê Hoàng C', '391234568', 'TK005'),
('GV004', 'Phạm Minh D', '0901234564', 'tk002'),
('GV005', 'Lê Văn Nhậu', '909876124', 'TK003'),
('GV006', 'Nguyễn Văn B', '967654368', 'TK008'),
('GV007', 'Bùi Thế G', '901234580', 'TK009'),
('GV008', 'Mai Thị H', '901234561', 'TK007'),
('GV009', 'Hồ Minh I', '901235671', 'TK010'),
('GV010', 'Ngô Thị J', '901234823', 'TK006');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hinhanh_sinhvien`
--

CREATE TABLE `hinhanh_sinhvien` (
  `masinhvien` varchar(20) DEFAULT NULL,
  `hinhanh` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `lop`
--

CREATE TABLE `lop` (
  `malop` varchar(10) NOT NULL,
  `tenlop` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `lop`
--

INSERT INTO `lop` (`malop`, `tenlop`) VALUES
('L001', 'Lop Toan'),
('L002', 'Lop Ly'),
('L003', 'CNTT'),
('L004', 'Kinh Tế'),
('L005', 'Việt Nam Học');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `quyen`
--

CREATE TABLE `quyen` (
  `maquyen` varchar(10) NOT NULL,
  `tenquyen` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `quyen`
--

INSERT INTO `quyen` (`maquyen`, `tenquyen`) VALUES
('Q001', 'Admin'),
('Q002', 'GiangVien'),
('Q003', 'SinhVien'),
('Q004', 'test1');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `quyen_chucnang`
--

CREATE TABLE `quyen_chucnang` (
  `maquyen` varchar(10) NOT NULL,
  `machucnang` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `quyen_chucnang`
--

INSERT INTO `quyen_chucnang` (`maquyen`, `machucnang`) VALUES
('Q001', 'CN001'),
('Q001', 'CN002'),
('Q001', 'CN003'),
('Q001', 'CN004'),
('Q001', 'CN005'),
('Q001', 'CN006'),
('Q001', 'CN007'),
('Q001', 'CN008'),
('Q002', 'CN001'),
('Q002', 'CN002'),
('Q002', 'CN004'),
('Q002', 'CN005'),
('Q002', 'CN006'),
('Q002', 'CN007'),
('Q002', 'CN008'),
('Q003', 'CN006'),
('Q003', 'CN008'),
('Q003', 'CN009');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sinhvien`
--

CREATE TABLE `sinhvien` (
  `masinhvien` varchar(255) NOT NULL,
  `hoten` varchar(255) NOT NULL,
  `malop` varchar(10) DEFAULT NULL,
  `cmnd` varchar(12) DEFAULT NULL,
  `gioitinh` varchar(12) DEFAULT NULL,
  `ngsinh` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `sodienthoai` varchar(15) DEFAULT NULL,
  `khoahoc` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `sinhvien`
--

INSERT INTO `sinhvien` (`masinhvien`, `hoten`, `malop`, `cmnd`, `gioitinh`, `ngsinh`, `email`, `sodienthoai`, `khoahoc`) VALUES
('SV001', 'Nguyễn Văn A', 'L001', '079203006451', 'Nam', '2000-01-01', 'nguyenvana@gmail.com', '909220021', '2000'),
('SV002', 'Trần Thị B', 'L002', '079203006455', 'Nam', '2001-02-02', 'tranthib@gmail.com', '909220031', '2000'),
('SV003', 'Lê Văn C', 'L001', '079203006452', 'Nam', '2000-03-03', 'levanc@gmail.com', '909220041', '2000'),
('SV004', 'Phạm Thị D', 'L001', '079203006456', 'Nam', '2002-04-04', 'phamthid@gmail.com', '909220051', '2000'),
('SV005', 'Nguyễn Văn A', 'L001', '079203006123', 'Nam', '2000-01-05', 'nguyenvana123@gmail.com', '0909220020', '2000'),
('SV006', 'Trần Thị Toản', 'L003', '079203006422', 'Nam', '2001-02-02', 'tranthib123@gmail.com', '0909220012', '2000'),
('SV3121330069', 'Bô Huệ Dinh', 'L003', '079203006321', 'Nữ', '2003-04-20', 'bohuedinh@gmail.com', '0901242512', '2000'),
('SV3121350016', 'Phan Thị Lan', 'L005', '079204006071', 'Nữ', '2003-10-22', 'phanthilan@gmail.com', '0902010247', '2000'),
('SV3121411206', 'Nguyễn Hoàng Tiến', 'L001', '079203006461', 'Nam', '2003-11-08', 'tienghe342@gmail.com', '0397387337', '2000');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `taikhoan`
--

CREATE TABLE `taikhoan` (
  `mataikhoan` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `matkhau` text NOT NULL,
  `maquyen` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `taikhoan`
--

INSERT INTO `taikhoan` (`mataikhoan`, `email`, `matkhau`, `maquyen`) VALUES
('TK001', 'admin@gmail.com', '12345678', 'Q001'),
('TK002', 'gv@gmail.com', '12345678', 'Q002'),
('TK003', 'sv@gmail.com', '12345678', 'Q003'),
('TK004', 'gv4@gmail.com', 'password4', 'Q002'),
('TK005', 'gv5@gmail.com', 'password5', 'Q002'),
('TK006', 'gv6@gmail.com', 'password6', 'Q002'),
('TK007', 'gv7@gmail.com', 'password7', 'Q002'),
('TK008', 'gv8@gmail.com', 'password8', 'Q002'),
('TK009', 'gv9@gmail.com', 'password9', 'Q002'),
('TK010', 'gv10@gmail.com', 'password10', 'Q002');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `buoihoc`
--
ALTER TABLE `buoihoc`
  ADD PRIMARY KEY (`mabuoihoc`),
  ADD KEY `malop` (`malop`),
  ADD KEY `buoihoc_ibfk_2` (`magiangvien`);

--
-- Chỉ mục cho bảng `chucnang`
--
ALTER TABLE `chucnang`
  ADD PRIMARY KEY (`machucnang`);

--
-- Chỉ mục cho bảng `diemdanh`
--
ALTER TABLE `diemdanh`
  ADD PRIMARY KEY (`madiemdanh`),
  ADD KEY `masinhvien` (`masinhvien`);

--
-- Chỉ mục cho bảng `giangvien`
--
ALTER TABLE `giangvien`
  ADD PRIMARY KEY (`magiangvien`),
  ADD KEY `mataikhoan` (`mataikhoan`);

--
-- Chỉ mục cho bảng `hinhanh_sinhvien`
--
ALTER TABLE `hinhanh_sinhvien`
  ADD KEY `masinhvien` (`masinhvien`);

--
-- Chỉ mục cho bảng `lop`
--
ALTER TABLE `lop`
  ADD PRIMARY KEY (`malop`);

--
-- Chỉ mục cho bảng `quyen`
--
ALTER TABLE `quyen`
  ADD PRIMARY KEY (`maquyen`);

--
-- Chỉ mục cho bảng `quyen_chucnang`
--
ALTER TABLE `quyen_chucnang`
  ADD PRIMARY KEY (`maquyen`,`machucnang`),
  ADD KEY `machucnang` (`machucnang`);

--
-- Chỉ mục cho bảng `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD PRIMARY KEY (`masinhvien`),
  ADD KEY `malop` (`malop`);

--
-- Chỉ mục cho bảng `taikhoan`
--
ALTER TABLE `taikhoan`
  ADD PRIMARY KEY (`mataikhoan`);

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `buoihoc`
--
ALTER TABLE `buoihoc`
  ADD CONSTRAINT `buoihoc_ibfk_1` FOREIGN KEY (`malop`) REFERENCES `lop` (`malop`),
  ADD CONSTRAINT `buoihoc_ibfk_2` FOREIGN KEY (`magiangvien`) REFERENCES `giangvien` (`magiangvien`) ON DELETE CASCADE;

--
-- Các ràng buộc cho bảng `diemdanh`
--
ALTER TABLE `diemdanh`
  ADD CONSTRAINT `diemdanh_ibfk_1` FOREIGN KEY (`masinhvien`) REFERENCES `sinhvien` (`masinhvien`);

--
-- Các ràng buộc cho bảng `giangvien`
--
ALTER TABLE `giangvien`
  ADD CONSTRAINT `giangvien_ibfk_1` FOREIGN KEY (`mataikhoan`) REFERENCES `taikhoan` (`mataikhoan`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Các ràng buộc cho bảng `hinhanh_sinhvien`
--
ALTER TABLE `hinhanh_sinhvien`
  ADD CONSTRAINT `hinhanh_sinhvien_ibfk_1` FOREIGN KEY (`masinhvien`) REFERENCES `sinhvien` (`masinhvien`);

--
-- Các ràng buộc cho bảng `quyen_chucnang`
--
ALTER TABLE `quyen_chucnang`
  ADD CONSTRAINT `quyen_chucnang_ibfk_1` FOREIGN KEY (`maquyen`) REFERENCES `quyen` (`maquyen`),
  ADD CONSTRAINT `quyen_chucnang_ibfk_2` FOREIGN KEY (`machucnang`) REFERENCES `chucnang` (`machucnang`);

--
-- Các ràng buộc cho bảng `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD CONSTRAINT `sinhvien_ibfk_1` FOREIGN KEY (`malop`) REFERENCES `lop` (`malop`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
