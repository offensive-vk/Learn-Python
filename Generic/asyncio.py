import asyncio
from dataclasses import dataclass
from abc import ABC

@dataclass(init=True, repr=True, frozen=True, slots=True)
class Program(ABC):
    @classmethod
    @staticmethod
    async def main[Type, Age](param: Type or str, age: Age) -> [Type, Age]:
        print(f"\r Hello .... Sir/Madam, {param} with age of {age}\n ... ")
        print(f"\v Type of param: {type(param)}\t & age: {type(age)}\n ....")
        await asyncio.sleep(1.5)
        print("\r ... World ....")
        await asyncio.sleep(1)
        print("\t ..... \t ....")
        await asyncio.sleep(1)
        print("\t ... Completed ... !")
        await asyncio.sleep(1.50)
        return [param, age]

if __name__ == "__main__":
    print("\n ============== \n")
    asyncio.run(Program.main("<; Madhav ; God ;>", 20))
    print(Program.__abstractmethods__)
    print("\n ============== \n")
