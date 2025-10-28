/** hof */
function hof(cb){
    cb()
}
function calculator(a,b,operation){
    return operation(a,b);
}

/** passing named function as callback function */
function sum(a,b){
    return a+b;
};
let res1=calculator(2,3,sum);
console.log(res1);