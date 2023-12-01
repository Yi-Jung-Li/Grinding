
(cl:in-package :asdf)

(defsystem "beginner_tutorials-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ask_BMI" :depends-on ("_package_ask_BMI"))
    (:file "_package_ask_BMI" :depends-on ("_package"))
  ))