-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 12, 2020 at 10:56 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `giftbasket`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE IF NOT EXISTS `cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `cart`
--


-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE IF NOT EXISTS `categories` (
  `catid` int(11) NOT NULL AUTO_INCREMENT,
  `catname` varchar(50) NOT NULL,
  PRIMARY KEY (`catid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`catid`, `catname`) VALUES
(1, 'Toys & Games'),
(2, 'Home & Living Gifts'),
(3, 'Fashion & Lifestyle Gifts'),
(4, 'Jewellery'),
(5, 'Gourmet');

-- --------------------------------------------------------

--
-- Table structure for table `customer_order`
--

CREATE TABLE IF NOT EXISTS `customer_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `p_price` int(11) NOT NULL,
  `p_qty` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `customer_order`
--

INSERT INTO `customer_order` (`id`, `cid`, `pid`, `p_price`, `p_qty`) VALUES
(1, 1, 5, 200, 1),
(2, 1, 6, 1040, 2);

-- --------------------------------------------------------

--
-- Table structure for table `cust_reg`
--

CREATE TABLE IF NOT EXISTS `cust_reg` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `cust_reg`
--

INSERT INTO `cust_reg` (`cid`, `cname`, `address`, `district`, `location`, `mobile`, `email`, `password`) VALUES
(1, 'Jithin', 'LCC', 'Ernakulam', 'Kochi', '9638527410', 'jithin@gmail.com', '123');

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

CREATE TABLE IF NOT EXISTS `events` (
  `eid` int(11) NOT NULL AUTO_INCREMENT,
  `events` varchar(50) NOT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `events`
--

INSERT INTO `events` (`eid`, `events`) VALUES
(1, 'Birthday'),
(2, 'Marriage'),
(3, 'Wedding Anniversary'),
(4, 'Baptism'),
(5, 'Valentines day');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `fdate` varchar(50) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`fid`, `cid`, `feedback`, `fdate`) VALUES
(1, 1, 'sss', '2020-02-04');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `uname` varchar(50) NOT NULL,
  `pass` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`uname`, `pass`, `utype`) VALUES
('jithin@gmail.com', '123', 'Customer'),
('admin@gmail.com', 'admin', 'Admin'),
('shyam@gmail.com', '123', 'Seller');

-- --------------------------------------------------------

--
-- Table structure for table `probooking`
--

CREATE TABLE IF NOT EXISTS `probooking` (
  `bid` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `bdate` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `probooking`
--

INSERT INTO `probooking` (`bid`, `pid`, `cid`, `bdate`, `status`) VALUES
(1, 1, 1, '2019-12-17', 'Paid'),
(2, 1, 1, '2019-12-23', 'Accept');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE IF NOT EXISTS `products` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `catid` int(11) NOT NULL,
  `subid` int(11) NOT NULL,
  `evid` int(11) NOT NULL,
  `pname` varchar(50) NOT NULL,
  `pdesc` varchar(4000) NOT NULL,
  `pimage` varchar(50) NOT NULL,
  `pamount` varchar(50) NOT NULL,
  `qty` int(11) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`pid`, `catid`, `subid`, `evid`, `pname`, `pdesc`, `pimage`, `pamount`, `qty`) VALUES
(5, 1, 1, 1, 'Beautiful Doll Designer Dress', 'Gorgeous and smart doll in mauve and white one piece beautiful dress and a stylish hair do. The doll is adorned with necklace and earrings for the perfect look and a great gift for your 3+ year old girl to play with.', 'static/media/SNAG-0027.jpg', '200', 20),
(6, 1, 1, 1, 'Chelsea in India Colours of India', 'Your little one will have not a better excitement to receive a gift of a cute Chelsea doll in colors of India. The gorgeous chelsea doll is an ideal gift for girls between 3-6 years and comes wearing a colorful and traditional Indian lehenga in red and gold with a veil on her head.', 'static/media/SNAG-0028.jpg', '520', 10),
(7, 2, 4, 3, 'Personalized LED Bottle Lamp', 'LED Bottle Lamp: In order to celebrate love and affection, gift this LED Bottle Lamp, this lamp can be personalised you need to send us the pictures and we would do the rest. You can gift this to your girlfriend, wife or to your sister as well.', 'static/media/SNAG-0029.jpg', '800', 15),
(8, 2, 4, 3, 'Colorful Rotating Crystal Cube with LED', 'A crystal cube with 4 LED rotates when an adapter is plugged in. In case, you don''t want to plug-in, AA batteries are an option that are not accompanied in the package.', 'static/media/SNAG-0030.jpg', '1200', 10),
(9, 5, 10, 1, 'Personalized Cadbury Celebrations Box', 'Remember the vows you took to love each other forever? Keep up with your promises as you rekindle the love with small gestures that go a long way. ', 'static/media/SNAG-0031.jpg', '250', 10);

-- --------------------------------------------------------

--
-- Table structure for table `staff_reg`
--

CREATE TABLE IF NOT EXISTS `staff_reg` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `staff_reg`
--

INSERT INTO `staff_reg` (`sid`, `sname`, `address`, `district`, `location`, `mobile`, `email`, `password`, `status`) VALUES
(1, 'Shyam', 'LCC', 'Ernakulam', 'Kochi', '8135674000', 'shyam@gmail.com', '123', 'Registered');

-- --------------------------------------------------------

--
-- Table structure for table `subcategory`
--

CREATE TABLE IF NOT EXISTS `subcategory` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `catid` int(11) NOT NULL,
  `sname` varchar(50) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `subcategory`
--

INSERT INTO `subcategory` (`sid`, `catid`, `sname`) VALUES
(1, 1, 'Dolls & Action Figures'),
(3, 1, 'Soft Toys'),
(4, 2, 'Home Decor Gifts'),
(5, 2, 'Furnishings'),
(6, 4, 'Earrings and Jhumkas'),
(7, 4, 'Pendants and Necklaces'),
(8, 5, 'Beverages'),
(9, 5, 'Sweets'),
(10, 5, 'Chocolates');
