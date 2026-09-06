import re

with open(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer\app\templates\invoice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Cart Table Wrapper
old_table = """            <div class="cart-table-wrapper">
                <table class="cart-table">
                    <thead>
                        <tr>
                            <th>رقم الصنف</th>
                            <th>الاسم</th>
                            <th>الكمية</th>
                            <th>السعر</th>
                            <th>الإجمالي</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody id="cart_body">
                        <!-- Items will be injected here -->
                    </tbody>
                </table>
            </div>"""

new_table = """            <div class="cart-table-wrapper" style="overflow-x: auto; font-size: 0.85rem;">
                <table class="cart-table" style="min-width: 800px; padding: 0;">
                    <thead>
                        <tr>
                            <th style="padding: 8px;">رقم الصنف</th>
                            <th style="padding: 8px;">الاسم</th>
                            <th style="padding: 8px;">الكمية</th>
                            <th style="padding: 8px;">السعر</th>
                            <th style="padding: 8px;">ن.خصم(%)</th>
                            <th style="padding: 8px;">الخصم</th>
                            <th style="padding: 8px;">الإجمالي</th>
                            <th style="padding: 8px;">الضريبة</th>
                            <th style="padding: 8px;">الصافي</th>
                            <th style="padding: 8px;"></th>
                        </tr>
                    </thead>
                    <tbody id="cart_body">
                        <!-- Items will be injected here -->
                    </tbody>
                </table>
            </div>"""
content = content.replace(old_table, new_table)

# 2. Add discount inputs to Item Details Modal
old_det_price = """                <div class="input-group">
                    <label>سعر البيع (للحبة)</label>
                    <input type="number" id="det_price" style="font-size: 1.5rem; text-align: center; font-weight: bold;" step="0.01">
                    <p id="det_min_price_warn" style="color: var(--danger); font-size: 0.8rem; margin-top: 0.5rem; display: none;">يجب ألا يقل السعر عن الحد الأدنى.</p>
                </div>"""

new_det_price = """                <div class="input-group">
                    <label>سعر البيع (للحبة)</label>
                    <input type="number" id="det_price" style="font-size: 1.5rem; text-align: center; font-weight: bold;" step="0.01">
                    <p id="det_min_price_warn" style="color: var(--danger); font-size: 0.8rem; margin-top: 0.5rem; display: none;">يجب ألا يقل السعر عن الحد الأدنى.</p>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                    <div class="input-group">
                        <label>نسبة خصم الحبة (%)</label>
                        <input type="number" id="det_disc_pct" value="0" min="0" max="100" style="font-size: 1.2rem; text-align: center;" onchange="calcItemDiscAmt()">
                    </div>
                    <div class="input-group">
                        <label>مبلغ خصم الحبة</label>
                        <input type="number" id="det_disc_amt" value="0" min="0" style="font-size: 1.2rem; text-align: center;" onchange="calcItemDiscPct()">
                    </div>
                </div>"""
content = content.replace(old_det_price, new_det_price)


# 3. JS changes
old_openItemDetails = """            document.getElementById('det_price').value = item.i_price;
            
            closeItemsModal();"""
new_openItemDetails = """            document.getElementById('det_price').value = item.i_price;
            document.getElementById('det_disc_pct').value = 0;
            document.getElementById('det_disc_amt').value = 0;
            
            closeItemsModal();"""
content = content.replace(old_openItemDetails, new_openItemDetails)

calc_fns = """        function calcItemDiscAmt() {
            const price = parseFloat(document.getElementById('det_price').value) || 0;
            const pct = parseFloat(document.getElementById('det_disc_pct').value) || 0;
            document.getElementById('det_disc_amt').value = (price * (pct / 100)).toFixed(2);
        }
        function calcItemDiscPct() {
            const price = parseFloat(document.getElementById('det_price').value) || 0;
            const amt = parseFloat(document.getElementById('det_disc_amt').value) || 0;
            if (price > 0) {
                document.getElementById('det_disc_pct').value = ((amt / price) * 100).toFixed(2);
            }
        }
"""
content = content.replace("function confirmAddItem() {", calc_fns + "\n        function confirmAddItem() {")

old_confirm_1 = """            const qty = parseFloat(document.getElementById('det_qty').value);
            const price = parseFloat(document.getElementById('det_price').value);
            const avail = parseFloat(currentSelectedItem.avail_qty);"""
new_confirm_1 = """            const qty = parseFloat(document.getElementById('det_qty').value);
            const price = parseFloat(document.getElementById('det_price').value);
            const disc_pct = parseFloat(document.getElementById('det_disc_pct').value) || 0;
            const disc_amt = parseFloat(document.getElementById('det_disc_amt').value) || 0;
            const avail = parseFloat(currentSelectedItem.avail_qty);"""
content = content.replace(old_confirm_1, new_confirm_1)

old_confirm_2 = """                cart[existingIdx].qty = newQty;
                cart[existingIdx].price = price;
            } else {
                cart.push({
                    i_code: currentSelectedItem.i_code,
                    i_name: currentSelectedItem.i_name,
                    qty: qty,
                    price: price
                });"""
new_confirm_2 = """                cart[existingIdx].qty = newQty;
                cart[existingIdx].price = price;
                cart[existingIdx].disc_pct = disc_pct;
                cart[existingIdx].disc_amt = disc_amt;
            } else {
                cart.push({
                    i_code: currentSelectedItem.i_code,
                    i_name: currentSelectedItem.i_name,
                    qty: qty,
                    price: price,
                    disc_pct: disc_pct,
                    disc_amt: disc_amt
                });"""
content = content.replace(old_confirm_2, new_confirm_2)


old_render = """        function renderCart() {
            const tbody = document.getElementById('cart_body');
            tbody.innerHTML = '';
            
            cart.forEach(item => {
                const tr = document.createElement('tr');
                const total = item.qty * item.price;
                tr.innerHTML = `
                    <td style="font-family: monospace; font-size: 0.9rem;">${item.i_code}</td>
                    <td style="font-weight: bold; color: var(--primary);">${item.i_name}</td>
                    <td>${item.qty}</td>
                    <td>${item.price.toFixed(2)}</td>
                    <td style="font-weight: bold;">${total.toFixed(2)}</td>
                    <td><button class="btn-danger" onclick="removeFromCart('${item.i_code}')">&times; حذف</button></td>
                `;
                tbody.appendChild(tr);
            });

            calculateTotals();
        }"""
new_render = """        function renderCart() {
            const tbody = document.getElementById('cart_body');
            tbody.innerHTML = '';
            
            cart.forEach(item => {
                const tr = document.createElement('tr');
                const total_before = item.qty * item.price;
                const total_disc = item.qty * (item.disc_amt || 0);
                const total_after_disc = total_before - total_disc;
                const total_vat = total_after_disc * 0.15;
                const net = total_after_disc + total_vat;
                
                tr.innerHTML = `
                    <td style="font-family: monospace; padding: 6px;">${item.i_code}</td>
                    <td style="font-weight: bold; color: var(--primary); padding: 6px;">${item.i_name}</td>
                    <td style="padding: 6px;">${item.qty}</td>
                    <td style="padding: 6px;">${item.price.toFixed(2)}</td>
                    <td style="padding: 6px; color: var(--danger);">${item.disc_pct || 0}%</td>
                    <td style="padding: 6px; color: var(--danger);">${(item.disc_amt || 0).toFixed(2)}</td>
                    <td style="padding: 6px;">${total_after_disc.toFixed(2)}</td>
                    <td style="padding: 6px;">${total_vat.toFixed(2)}</td>
                    <td style="font-weight: bold; padding: 6px;">${net.toFixed(2)}</td>
                    <td style="padding: 6px;"><button class="btn-danger" style="padding: 4px 8px; font-size: 0.8rem;" onclick="removeFromCart('${item.i_code}')">&times; حذف</button></td>
                `;
                tbody.appendChild(tr);
            });

            calculateTotals();
        }"""
content = content.replace(old_render, new_render)

old_subtotal_calc_1 = "cart.forEach(item => { subtotal += (item.qty * item.price); });"
new_subtotal_calc_1 = "cart.forEach(item => { subtotal += (item.qty * (item.price - (item.disc_amt || 0))); });"
content = content.replace(old_subtotal_calc_1, new_subtotal_calc_1)


with open(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer\app\templates\invoice.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
