(defun get-file (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
          while line
          collect line)))

(defun to-integer-list (str)
  (loop for i in (coerce str 'list)
        collect (digit-char-p i)))

(defun solution (path)
 (loop for preline in (get-file path)
       do (let ((line (to-integer-list preline)))
            (loop for num in line
                    with tens = 0
                    with ones = 0
                    with index = 0
             do (case (and (> num tens)
                           (<= index (- 1 (list-length line)))
                           ((setf tens num) (setf ones 0)))
                  ((> num ones) (setf ones num))
                  (setf index (1+ index))
                  (print (+ (* tens 10) ones)))))))
             
            

(solution "test_input.txt")
