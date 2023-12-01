// Generated by gencpp from file tm_msgs/robot_motion.msg
// DO NOT EDIT!


#ifndef TM_MSGS_MESSAGE_ROBOT_MOTION_H
#define TM_MSGS_MESSAGE_ROBOT_MOTION_H

#include <ros/service_traits.h>


#include <tm_msgs/robot_motionRequest.h>
#include <tm_msgs/robot_motionResponse.h>


namespace tm_msgs
{

struct robot_motion
{

typedef robot_motionRequest Request;
typedef robot_motionResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct robot_motion
} // namespace tm_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::tm_msgs::robot_motion > {
  static const char* value()
  {
    return "8e3073766aab12c61a8c47f8c01da720";
  }

  static const char* value(const ::tm_msgs::robot_motion&) { return value(); }
};

template<>
struct DataType< ::tm_msgs::robot_motion > {
  static const char* value()
  {
    return "tm_msgs/robot_motion";
  }

  static const char* value(const ::tm_msgs::robot_motion&) { return value(); }
};


// service_traits::MD5Sum< ::tm_msgs::robot_motionRequest> should match
// service_traits::MD5Sum< ::tm_msgs::robot_motion >
template<>
struct MD5Sum< ::tm_msgs::robot_motionRequest>
{
  static const char* value()
  {
    return MD5Sum< ::tm_msgs::robot_motion >::value();
  }
  static const char* value(const ::tm_msgs::robot_motionRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::tm_msgs::robot_motionRequest> should match
// service_traits::DataType< ::tm_msgs::robot_motion >
template<>
struct DataType< ::tm_msgs::robot_motionRequest>
{
  static const char* value()
  {
    return DataType< ::tm_msgs::robot_motion >::value();
  }
  static const char* value(const ::tm_msgs::robot_motionRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::tm_msgs::robot_motionResponse> should match
// service_traits::MD5Sum< ::tm_msgs::robot_motion >
template<>
struct MD5Sum< ::tm_msgs::robot_motionResponse>
{
  static const char* value()
  {
    return MD5Sum< ::tm_msgs::robot_motion >::value();
  }
  static const char* value(const ::tm_msgs::robot_motionResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::tm_msgs::robot_motionResponse> should match
// service_traits::DataType< ::tm_msgs::robot_motion >
template<>
struct DataType< ::tm_msgs::robot_motionResponse>
{
  static const char* value()
  {
    return DataType< ::tm_msgs::robot_motion >::value();
  }
  static const char* value(const ::tm_msgs::robot_motionResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // TM_MSGS_MESSAGE_ROBOT_MOTION_H
