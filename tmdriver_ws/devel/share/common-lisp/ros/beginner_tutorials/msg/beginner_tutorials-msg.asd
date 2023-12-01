
(cl:in-package :asdf)

(defsystem "beginner_tutorials-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "my_info" :depends-on ("_package_my_info"))
    (:file "_package_my_info" :depends-on ("_package"))
  ))