; Q4
(define (rle s)
  (define (helper s last cnt)
    (cond
      ((null? s) (cons-stream (list last cnt) nil))
      ((= last (car s)) (helper (cdr-stream s) (car s) (+ cnt 1)))
      (else (cons-stream (cons last (cons cnt nil)) (helper (cdr-stream s) (car s) 1)))
    )
  )
  (if (null? s) () (helper (cdr-stream s) (car s) 1))
)

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
(define (insert n s)
  (define (helper n s res)
    (cond
      ((null? s) (append res (cons n nil)))
      ((<= n (car s)) (append (append res (cons n nil)) s))
      (else (helper n (cdr s) (append res (cons (car s) nil))))
    )
  )
  (if (< n (car s))
    (append (cons n nil) s)
    (helper n (cdr s) (cons (car s) nil))
  )
)

; Q6
(define (deep-map fn s)
  (cond
    ((null? s) nil)
    ((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
    (else (cons (fn (car s)) (deep-map fn (cdr s))))
  )
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
  (define (in-a-list? a res)
    (cond
      ((null? res) #f)
      ((eq? a (car res)) #t)
      (else (in-a-list? a (cdr res)))
    )
  )
  (define (pick-unique res s)
    (cond
      ((null? s) res)
      ((in-a-list? (car s) res) (pick-unique res (cdr s)))
      (else (pick-unique (append res (cons (car s) nil)) (cdr s)))
    )
  )
  (pick-unique () s)
)

(define (count name s)
  (define (helper name s cnt)
    (cond
      ((null? s) cnt)
      ((eq? name (car s)) (helper name (cdr s) (+ cnt 1)))
      (else (helper name (cdr s) cnt))
    )
  )
  (helper name s 0)
)

(define (tally names)
  (define unique-dict (unique names))
  (define (helper names unique-dict)
    (if (null? unique-dict) nil
      (cons (cons (car unique-dict) (count (car unique-dict) names)) (helper names (cdr unique-dict)))
    )
  )
  (helper names unique-dict)
)
