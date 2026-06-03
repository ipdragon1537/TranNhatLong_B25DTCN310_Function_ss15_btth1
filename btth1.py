inventory_stock = 100
total_revenue = 0
def add_stock():
    amount = int(input("Nhập số lượng hàng muốn thêm vào kho: "))
    global inventory_stock
    inventory_stock += amount
    print(f"Đã thêm {amount} sản phẩm và kho.")
    print(f"Tồn kho hiện tại:{inventory_stock}")
def process_sale():
    """
    Chức năng bán hàng.
    Input:
        Người dùng nhập:
        - quantity: số lượng sản phẩm mua
        - price: giá bán mỗi sản phẩm
    Return:
        Không trả về giá trị nào (None).
        Cập nhật tồn kho và tổng doanh thu."""
    global inventory_stock
    global total_revenue
    print("--- BÁN HÀNG ---")
    quantity = int(input("Nhập số lượng mua: "))
    price = float(input("Nhập giá bán: "))
    if inventory_stock < 0:
        print("Không đủ hàng trong kho!")
        return
    elif quantity > inventory_stock:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}")
        return
    else:
        print(f"Số lượng:{quantity} | Đơn giá:{price}")
        final_price =calculate_final_price(quantity, price)
        inventory_stock -= quantity
        total_revenue += final_price
def calculate_final_price(quantity, price):
    '''
    Tính tổng tiền thanh toán cho đơn hàng.
    Parameters:
        quantity (int): Số lượng sản phẩm mua.
        price (float): Giá bán của một sản phẩm.
    Returns:
        float: Tổng tiền cuối cùng sau giảm giá và VAT.'''
    discount_fee = 0
    total_price = quantity * price
    if total_price >= 1000:
       discount_fee = total_price * 0.1
    total_after_discount = total_price - discount_fee
    vat_price = 0.08 * total_after_discount
    final_price = total_after_discount + vat_price
    print(f"Tạm tính:${total_price}")
    print(f"Giảm giá (10%):{discount_fee}")
    print(f"Thuế VAT (8%):{vat_price}")
    print(f"Tổng tiền thanh toán:{final_price}")
    return final_price
def print_report():
    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại:{inventory_stock}")
    print(f"Tổng doanh thu:{total_revenue}")
def main():
    while True:
        print("""========== TECHSTORE MANAGEMENT SYSTEM ==========
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
=================================================
Chọn chức năng (1-4):""")
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                add_stock()
            case "2":
                process_sale()
            case "3":
                print_report()
            case "4":
                print("Thoát chương trình")
                break
            case _:
                print("Lựa chọn ko hợp lệ")
main()
