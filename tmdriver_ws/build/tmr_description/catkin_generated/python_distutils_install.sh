#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/biorola/tmdriver_ws/src/tmr_description"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/biorola/tmdriver_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/biorola/tmdriver_ws/install/lib/python2.7/dist-packages:/home/biorola/tmdriver_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/biorola/tmdriver_ws/build" \
    "/usr/bin/python2" \
    "/home/biorola/tmdriver_ws/src/tmr_description/setup.py" \
     \
    build --build-base "/home/biorola/tmdriver_ws/build/tmr_description" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/biorola/tmdriver_ws/install" --install-scripts="/home/biorola/tmdriver_ws/install/bin"
