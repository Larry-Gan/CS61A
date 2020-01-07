;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond
      ((< x 0) -1)
        ((> x 0) 1)
        ((= x 0) 0)
)
)

(define (square x) (* x x))

(define (pow b n)
  (cond
        ((= n 0) 1)
        ((even? n) (* (square b) (pow b (- n 2))))
        ((odd? n) (* b (pow b (- n 1))))
  )
)

(define (unique s)
    (if (null? s) ()
      (cons (car s) (unique (filter (lambda (c) (not (eq? c (car s)))) s)))

    )
    )
