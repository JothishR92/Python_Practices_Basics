*** Settings ***
library  main.py

*** Variables ***
${a}    10
${b}    10
${c}    10
${d}    10

*** Test Cases ***
Addition of code
    ${value}=   main.add    ${a}    ${b}
    ${value2}=  Evaluate    ${c}+${d}
    Should Be Equal     ${value2}   ${value}