// Generated by gencpp from file tm_msgs/robot_stateRequest.msg
// DO NOT EDIT!


#ifndef TM_MSGS_MESSAGE_ROBOT_STATEREQUEST_H
#define TM_MSGS_MESSAGE_ROBOT_STATEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace tm_msgs
{
template <class ContainerAllocator>
struct robot_stateRequest_
{
  typedef robot_stateRequest_<ContainerAllocator> Type;

  robot_stateRequest_()
    : state(0)  {
    }
  robot_stateRequest_(const ContainerAllocator& _alloc)
    : state(0)  {
  (void)_alloc;
    }



   typedef int8_t _state_type;
  _state_type state;





  typedef boost::shared_ptr< ::tm_msgs::robot_stateRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::tm_msgs::robot_stateRequest_<ContainerAllocator> const> ConstPtr;

}; // struct robot_stateRequest_

typedef ::tm_msgs::robot_stateRequest_<std::allocator<void> > robot_stateRequest;

typedef boost::shared_ptr< ::tm_msgs::robot_stateRequest > robot_stateRequestPtr;
typedef boost::shared_ptr< ::tm_msgs::robot_stateRequest const> robot_stateRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::tm_msgs::robot_stateRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::tm_msgs::robot_stateRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::tm_msgs::robot_stateRequest_<ContainerAllocator1> & lhs, const ::tm_msgs::robot_stateRequest_<ContainerAllocator2> & rhs)
{
  return lhs.state == rhs.state;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::tm_msgs::robot_stateRequest_<ContainerAllocator1> & lhs, const ::tm_msgs::robot_stateRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace tm_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::tm_msgs::robot_stateRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::tm_msgs::robot_stateRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::tm_msgs::robot_stateRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::tm_msgs::robot_stateRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tm_msgs::robot_stateRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tm_msgs::robot_stateRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::tm_msgs::robot_stateRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a33bed68685ae53bd39b0a9242210752";
  }

  static const char* value(const ::tm_msgs::robot_stateRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa33bed68685ae53bULL;
  static const uint64_t static_value2 = 0xd39b0a9242210752ULL;
};

template<class ContainerAllocator>
struct DataType< ::tm_msgs::robot_stateRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "tm_msgs/robot_stateRequest";
  }

  static const char* value(const ::tm_msgs::robot_stateRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::tm_msgs::robot_stateRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int8 state\n"
;
  }

  static const char* value(const ::tm_msgs::robot_stateRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::tm_msgs::robot_stateRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.state);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct robot_stateRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::tm_msgs::robot_stateRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::tm_msgs::robot_stateRequest_<ContainerAllocator>& v)
  {
    s << indent << "state: ";
    Printer<int8_t>::stream(s, indent + "  ", v.state);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TM_MSGS_MESSAGE_ROBOT_STATEREQUEST_H
