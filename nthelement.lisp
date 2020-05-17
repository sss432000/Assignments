;finding nth element from a list

(write "Enter the number of element between 1 to 10 to be found")
(terpri)
(setq n (read))
(setf a (list 10 20 30 40 50 60 70 80 90 100))
(write "The nth element is :")
(write (nth (- n 1) a))

