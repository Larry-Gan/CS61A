; Macros

(define-macro (for sym vals expr)
  (list 'map (list 'lambda (list sym) expr) vals)
)



(define-macro (list-of map-expr for var in lst if filter-expr)
  (list 'map (list 'lambda `(,var) map-expr) (list 'filter (list 'lambda `(,var) filter-expr) lst))

)

'(var)
(var)
(list var)
(x)
