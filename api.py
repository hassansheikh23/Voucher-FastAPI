from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import pipeline.pipeline as pl


class VoucherRequest(BaseModel):
    customer_id: int
    country_code: str
    last_order_ts: datetime
    first_order_ts: datetime
    total_orders: int
    segment_name: str

class VoucherResponse(BaseModel):
    voucher_amount: int = -1
    detail: str = None


app = FastAPI()


@app.post("/api/voucher/", response_model = VoucherResponse, response_model_exclude_unset=True)
def get_voucher(voucher_request: VoucherRequest):
    conn = pl.get_connection()
    voucher_response = pl.get_voucher(conn, voucher_request.dict())
    return voucher_response