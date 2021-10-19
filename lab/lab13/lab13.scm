; Q1
(define (compose-all funcs)
  (cond
    ((null? funcs) (lambda (x) x))
    (else (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x))))
  )
)

; Q2
(define (tail-replicate x n)
  (define (helper res x n)
    (cond
      ((= n 0) res)
      (else (helper (cons x res) x (- n 1)))
    )
  )
  (helper () x n)
)
