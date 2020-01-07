; Lab 14: Final Review

(define (compose-all funcs)
  (lambda (x)
    (cond
      ((null? funcs) x)
      (else ((compose-all (cdr funcs)) ((car funcs) x)))
    )
  )

)

(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? seen-so-far) #f)
          ((contains? curr (car seen-so-far)) #t)
          (else (pair-tracker (cdr-stream seen-so-far) (cons-stream (car seen-so-far) curr))))
    )
  (pair-tracker s nil)
)

(define (contains? lst s)
  (cond
    ((null? lst) #f)
    ((eq? (car lst) s) #t)
    (else (contains? (cdr-stream lst) s))
  )
)
