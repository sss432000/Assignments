;factorial without recurssion

(setf res 1) 
(defun factorial (num)(loop for i from 1 to n
       do(setf res (* res i )))
       (setf n res))

(write "Enter the value of n")
(terpri)
(setq n (read))
(write "Factorial is :")
(write (factorial n))

