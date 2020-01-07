
; Tail recursion

(define (replicate x n)
  (define (helper x n count)
    (cond
      ((eq? n 0) count)
      (else (helper x (- n 1) (cons x count)))
    )
  )
  (helper x n '())
)

(define (accumulate combiner start n term)
  (cond
    ((= n 0) start)
    (else (combiner (term n) (accumulate combiner start (- n 1) term)))
  )
)

(define (accumulate-tail combiner start n term)
  (define (helper combiner start n term count)
    (cond
      ((= n 0) count)
      (else (helper combiner start (- n 1) term (combiner (term n) count)))
    )
  )
  (helper combiner start n term start)
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (cons-stream 3 (map-stream (lambda (x) (+ x 3)) multiples-of-three))
)

(define (helper s cur rec)
  (cond
    ((eq? s nil) cur)
    ((eq? cur nil) (helper (cdr-stream s) (cons (car s) nil) (car s)))
    ((< (car s) rec) cur)
    (else (helper (cdr-stream s) (append cur (list (car s))) (car s)))
  )
)
(define (nondec s rec)
  (cond
    ((eq? s nil) nil)
    ((> rec (car s)) s)
    (else (nondec (cdr-stream s) (car s)))
  )
)
(define (nondecreastream s)
  (define first (helper s nil -100))
  (if (eq? first nil) nil
    (cons-stream first (nondecreastream (nondec s -100)))
  )
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))
