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
            (print line))))
            

(solution "test_input.txt")
