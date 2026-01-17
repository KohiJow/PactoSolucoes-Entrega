import re
from playwright.sync_api import Page, expect

def test_pacto_solucoes_yahoo(page: Page):
    page.goto("https://br.search.yahoo.com/?fr2=p:fprd,mkt:br")
    
    page.get_by_placeholder("Buscar na Web").fill("Pacto Soluções")
    
    page.get_by_text("Pacto Soluções").first.click()
    
    page.wait_for_timeout(2000)
    try:
        page.get_by_role("button", name="OK").click()
    except:
        pass

    expect(page).to_have_url(re.compile(r"p=pacto"))
    
    expect(page.get_by_text("Pacto Soluções").first).to_be_visible()
    
    
    expect(page.locator('[data-matarget="algo"]')).to_have_count_greater_than(0)
    expect(page.locator('a.fz-20:has-text("Pacto")')).to_be_visible()
