from requests_pack.submit_order import submit_order


class TestSubmitOrder:
		def test_submit_order(self):
				response = submit_order(2,"Andrei")
				assert response.status_code == 201,f"Error: Status code is not valid. Expected: 201, actual: {response.status_code}"
				assert response.json()["created"]==True, f"Error: Order creation status is not correct. Expected: True, Actual: {response.json()['created']}"
				assert len(response.json()["orderId"])>0, f"Error: Order id is invalid. Expected lenght greater than zero. Actual length: {len(response.json()['orderId'])}"

		def test_submit_oder_invalid_error_msg(self):
				make_request = submit_order(1003, "John")
				assert make_request.json()["error"] == 'Invalid or missing bookId.'
