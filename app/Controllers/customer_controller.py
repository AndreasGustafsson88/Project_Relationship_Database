import Data.Repository.company_customer_repository as ccr
import Data.Repository.private_customer_repository as pcr


def get_all_customers():
    company_customer= ccr.get_company_customer()
    private_customer = pcr.get_private_customer()
    return company_customer+private_customer


def get_customer_by_id():
    pass


