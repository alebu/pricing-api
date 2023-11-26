from fastapi import FastAPI
from pydantic import BaseModel
from src.pricing import call_option_bsm_formula

class User_input(BaseModel):
    S : float
    K : float
    T: float 
    t: float
    r: float 
    sigma: float

app = FastAPI()

@app.post('/calculate')
def operate(input:User_input):
    pr = call_option_bsm_formula(input.S, input.K, input.T, input.t, input.r, input.sigma)
    return round(pr, 3) 

