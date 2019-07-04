addLema(Formula):-
    parse(Formula, AST),
    check(AST),
    prove(AST),
    asserta(lemma(AST)).

addAxiom(Formula):-
    parse(Formula, AST),
    check(AST),
    asserta(axiom(AST)).

query(Formula):-
    parse(Formula, AST),
    check(AST),
    prove(AST).

parse(Formula, AST) :-
    parseString(Formula, Parsed),
    getAST(Parsed, AST).

getAST(Formula, AST) :-
    ["forall", Variable | Other] = Formula,
    getVariableWithoutDot(Variable, SanitizatedVariable),
    getAST(Other, OtherAST),
    AST = forall(SanitizatedVariable, OtherAST),
    !.
    
getAST(Formula, AST) :-
    ["exists", Variable | Other] = Formula,
    getVariableWithoutDot(Variable, SanitizatedVariable),
    getAST(Other, OtherAST),
    AST = exists(SanitizatedVariable, OtherAST),
    !.

getAST(Formula, AST) :-
    ["not" | OtherFormula] = Formula,
    getAST(OtherFormula, OtherAST),
    AST = not(OtherAST),
    !.

getAST(Formula, AST):-
    parseBinary(Formula, Left, "and", Right), 
    !,
    getAST(Left, LeftAST),
    getAST(Right, RightAST),
    AST = and(LeftAST, RightAST).

getAST(Formula, AST):-
    parseBinary(Formula, Left, "or", Right), 
    !,
    getAST(Left, LeftAST),
    getAST(Right, RightAST),
    AST = or(LeftAST, RightAST).

getAST(Formula, AST):-
    parseBinary(Formula, Left, "implies", Right), 
    getAST(Left, LeftAST),
    getAST(Right, RightAST),
    AST = implies(LeftAST, RightAST).
    

getAST(Formula, AST) :-
    [ First | Other] = Formula,
    sub_string(First, 1, _, 0, Predicate),
    cleanLastItem(Other, CleanOther),
    getAST([Predicate | CleanOther], AST),
    !.

getAST(Formula,AST):-
    [Predicate] = Formula,
    getPredicate(Predicate, Name, Term),
    getASTTerm([Term], TermAST),
    AST = predicate(Name, TermAST),
    !.

getAST(Formula,AST):-
    [Predicate] = Formula,
    AST = predicate(Predicate, void).

parseString(StringFormula, Formula):- 
    split_string(StringFormula, " ", "", Formula).

getPredicate(Predicate, Name, Variable):-
    sub_string(Predicate, Before, _, After, "("), !,
    sub_string(Predicate, 0, Before, _, PredicateName),
    atom_string(PredicateName, Name),
    sub_string(Predicate, After,_, 1, VariableName),
    atom_string(VariableName, Variable).

getVariableWithoutDot(Variable, SanitizatedVariable):-
    sub_string(Variable, Before, _, 0, "."), !,
    sub_string(Variable, 0, Before, _, SanitizatedVariable).


parseBinary(Formula, Left, Op, Right) :-
    [FirstBlock | Other] = Formula,
    sub_string(FirstBlock, 0, 1, _, "("), !,
    nextParenthesis(Formula, Index),
    sub_list(Formula, Index, Left, [Op | Right]).

parseBinary(Formula, [FirstBlock], Op, Right) :-
    [FirstBlock, Op | Right ] = Formula,
    sub_string(FirstBlock, 0, 1, _, "("), !,
    sub_string(FirstBlock, _, 1, 0, ")").

parseBinary(Formula, [Left], Op, Right) :-
    [Left, Op | Right] = Formula.

sub_list(List, Index, [ Element | SublistBefore], SubListAfter) :-
    Index > 0,
    List = [ Element | Next ],
    NewIndex is Index-1,
    sub_list(Next, NewIndex, SublistBefore ,SubListAfter).

sub_list(List, 0, [], List).

nextParenthesis(Formula, 1) :-
    [ FirstItem | _ ] = Formula,
    countOcurrences(FirstItem, ")", CloseOcurrences),
    countOcurrences(FirstItem, "(", OpenOcurrences),
    CloseOcurrences > OpenOcurrences.
    
nextParenthesis(Formula, Index) :-
    [ _ | Resto ] = Formula,
    nextParenthesis(Resto, RestoIndex),
    Index is RestoIndex + 1.

countOcurrences(String, Character, Ocurrences) :-
    split_string(String, Character, "", ListSubStrings),
    length(ListSubStrings, ListLength),
    Ocurrences is ListLength - 1.


cleanLastItem(List, [CleanString]) :-
    [LastItem] = List,
    sub_string(LastItem, 0, _, 1, CleanString).
    

cleanLastItem(List, [Item | CleanOther]) :-
    [Item|Other] = List,
    cleanLastItem(Other, CleanOther).

getASTTerm([Term], TermAST):-
    TermAST = variable(Term).

check(Formula):-
    forall( _ , OtherFormula) = Formula,
    check(OtherFormula).

check(Formula):-
    exists( _ , OtherFormula) = Formula,
    check(OtherFormula).

check(Formula):-
    not(OtherFormula) = Formula,
    check(OtherFormula).

check(Formula):-
    and(Left, Right) = Formula,
    check(Left),
    check(Right).

check(Formula):-
    or(Left, Right) = Formula,
    check(Left),
    check(Right).

check(Formula):-
    implies(Left, Right) = Formula,
    check(Left),
    check(Right).

check(Formula):-
    predicate(_,_) = Formula.
