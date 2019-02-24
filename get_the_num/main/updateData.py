from inserLosingLotteryData import updateLosingLottery
from insertThripleNum import updateThripleData
from inserDHRData import updateDHR
from insertPairNum import updatePairData
from insertSSQData import updateSSQData
def updateData():
    # 更新最新的数据
    updateSSQData()
    # 更新遗漏表
    updateLosingLottery()
    # 更新DHR
    updateDHR()
    # 更新成对数据
    updatePairData()
    # 更新一组3号数据
    updateThripleData()
if __name__ =='__main__':
    # 更新最新的数据
    updateData()