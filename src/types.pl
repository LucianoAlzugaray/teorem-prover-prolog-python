% Quantifiers
type(forall( _, _ ), quantifier)
type(forall( _, _ ), formula)
type(exists( _, _ ), quantifier)
type(exists( _, _ ), formula)

% Terms
type(variable(_), term)
type(function(_), term)

% Formulae
type(not(_), formula)
type(or(_,_), formula)
type(and(_,_), formula)
type(and(_,_), formula)
