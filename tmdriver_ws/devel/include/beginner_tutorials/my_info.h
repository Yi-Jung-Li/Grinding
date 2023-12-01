// Generated by gencpp from file beginner_tutorials/my_info.msg
// DO NOT EDIT!


#ifndef BEGINNER_TUTORIALS_MESSAGE_MY_INFO_H
#define BEGINNER_TUTORIALS_MESSAGE_MY_INFO_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace beginner_tutorials
{
template <class ContainerAllocator>
struct my_info_
{
  typedef my_info_<ContainerAllocator> Type;

  my_info_()
    : name()
    , height(0.0)
    , weight(0.0)  {
    }
  my_info_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , height(0.0)
    , weight(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  _name_type name;

   typedef float _height_type;
  _height_type height;

   typedef float _weight_type;
  _weight_type weight;





  typedef boost::shared_ptr< ::beginner_tutorials::my_info_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::beginner_tutorials::my_info_<ContainerAllocator> const> ConstPtr;

}; // struct my_info_

typedef ::beginner_tutorials::my_info_<std::allocator<void> > my_info;

typedef boost::shared_ptr< ::beginner_tutorials::my_info > my_infoPtr;
typedef boost::shared_ptr< ::beginner_tutorials::my_info const> my_infoConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::beginner_tutorials::my_info_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::beginner_tutorials::my_info_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::beginner_tutorials::my_info_<ContainerAllocator1> & lhs, const ::beginner_tutorials::my_info_<ContainerAllocator2> & rhs)
{
  return lhs.name == rhs.name &&
    lhs.height == rhs.height &&
    lhs.weight == rhs.weight;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::beginner_tutorials::my_info_<ContainerAllocator1> & lhs, const ::beginner_tutorials::my_info_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace beginner_tutorials

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::beginner_tutorials::my_info_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::beginner_tutorials::my_info_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::beginner_tutorials::my_info_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::beginner_tutorials::my_info_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::beginner_tutorials::my_info_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::beginner_tutorials::my_info_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::beginner_tutorials::my_info_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f8b3f5b2c4ae2022214645498883c09b";
  }

  static const char* value(const ::beginner_tutorials::my_info_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf8b3f5b2c4ae2022ULL;
  static const uint64_t static_value2 = 0x214645498883c09bULL;
};

template<class ContainerAllocator>
struct DataType< ::beginner_tutorials::my_info_<ContainerAllocator> >
{
  static const char* value()
  {
    return "beginner_tutorials/my_info";
  }

  static const char* value(const ::beginner_tutorials::my_info_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::beginner_tutorials::my_info_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string name\n"
"float32 height\n"
"float32 weight\n"
;
  }

  static const char* value(const ::beginner_tutorials::my_info_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::beginner_tutorials::my_info_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.height);
      stream.next(m.weight);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct my_info_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::beginner_tutorials::my_info_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::beginner_tutorials::my_info_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "height: ";
    Printer<float>::stream(s, indent + "  ", v.height);
    s << indent << "weight: ";
    Printer<float>::stream(s, indent + "  ", v.weight);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BEGINNER_TUTORIALS_MESSAGE_MY_INFO_H
