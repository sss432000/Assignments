;factorial with recurssion

(defun factorial (num)
   (cond ((zerop num) 1)   ;checks condition if number is 0 it returns 1
      (t ( * num (factorial (- num 1))))     ;use logic n! = n*(n-1)*(n-2).....
   )
)

(write "Enter the value of n")
(terpri)
(setq n (read))
(format t "Factorial of ~d is: ~d" n (factorial n))
