from core import exceptions
from core import error
import random
import time
import API
import os

class TestAPI:
    curpath = os.getcwd()
    curpath += '/'
    testModule = "sample"
    testService = "sample"
    searchString = "recon"
    seed = random.randint(111111, 999999)

    def test_NewModuleGeneration(self):
        API.ShadowSuite().generate_new_module(str(self.seed))
        if os.path.exists(self.curpath + "/output/" + str(self.seed) + '.py'):
            os.remove(self.curpath + "/output/" + str(self.seed) + '.py')

        else:
            raise exceptions.ModuleGenerationError("Generated Module Not Found!")

    def test_NewServiceGeneration(self):
        API.ShadowSuite().generate_new_service(str(self.seed))
        if os.path.exists(self.curpath + "/output/" + str(self.seed) + '.py'):
            os.remove(self.curpath + "/output/" + str(self.seed) + '.py')

        else:
            raise exceptions.ServiceGenerationError("Generated Service Not Found!")

    def test_ModuleListing(self):
        API.ShadowSuite().list_module()

    def test_ServiceListing(self):
        API.ShadowSuite().list_services()

    def test_ModuleFinding(self):
        API.ShadowSuite().find_module(self.testModule)

    def test_ServiceFinding(self):
        API.ShadowSuite().find_service(self.testService)

    def test_UseModule(self):
        API.ShadowSuite().use_module(self.testModule)

    def test_UseService(self):
        API.ShadowSuite().use_service(self.testService)

    def test_Suggest(self):
        API.ShadowSuite().suggest(self.searchString)

    def test_ClearScreen(self):
        API.ShadowSuite().clrscrn()

def main():
    TestAPI().test_NewModuleGeneration()
    time.sleep(1)
    TestAPI().test_NewServiceGeneration()
    time.sleep(1)
    TestAPI().test_ModuleListing()
    time.sleep(1)
    TestAPI().test_ServiceListing()
    time.sleep(1)
    TestAPI().test_ModuleFinding()
    time.sleep(1)
    TestAPI().test_ServiceFinding()
    time.sleep(1)
    TestAPI().test_UseModule()
    time.sleep(1)
    TestAPI().test_UseService()
    time.sleep(1)
    TestAPI().test_Suggest()
    time.sleep(1)
    TestAPI().test_ClearScreen()
    time.sleep(1)
    TestAPI().test_NewServiceGeneration()
    time.sleep(1)
    TestAPI().test_ModuleListing()
    time.sleep(1)
    TestAPI().test_ServiceListing()
    time.sleep(1)
    TestAPI().test_ModuleFinding()
    time.sleep(1)
    TestAPI().test_ServiceFinding()
    time.sleep(1)
    TestAPI().test_UseModule()
    time.sleep(1)
    TestAPI().test_UseService()
    time.sleep(1)
    TestAPI().test_Suggest()
    time.sleep(1)
    TestAPI().test_ClearScreen()
    time.sleep(1)

    # Test if error codes exists...
    errorCodes = [error.errorCodes().ERROR0001, error.errorCodes().ERROR0002, \
            error.errorCodes().ERROR0003, error.errorCodes().ERROR0004, \
            error.errorCodes().ERROR0005, error.errorCodes().ERROR0006, \
            error.errorCodes().ERROR0007, error.errorCodes().ERROR0008, \
            error.errorCodes().ERROR0009, error.errorCodes().ERROR0010, \
            error.errorCodes().ERROR0011("3.6.1"), error.errorCodes().ERROR0012, \
            error.errorCodes().ERROR0013, error.errorCodes().ERROR0014, \
            error.errorCodes().ERROR0015, error.errorCodes().ERROR0016, \
            error.errorCodes().ERROR0017, error.errorCodes().ERROR0018, \
            error.errorCodes().ERROR0019, error.errorCodes().ERROR0020('TestingErrorCodes'), \
            error.errorCodes().ERROR0021
            ]
    
    # Test if warning codes exists...
    warningCodes = [error.warningCodes().WARNING0001, error.warningCodes().WARNING0002, \
            error.warningCodes().WARNING0003, error.warningCodes().WARNING0004, \
            error.warningCodes().WARNING0005, error.warningCodes().WARNING0006
            ]
    
    # Test if HTTP codes exists...
    HTTPErrors = [error.HTTPCodes().info_100, error.HTTPCodes().info_101
            ]

if __name__ == '__main__':
    main()
