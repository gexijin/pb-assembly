#!/usr/bin/env
import unittest

from utils import load_results
import test_asm
import test_preassembly

class TestYeastAsm(test_asm.TestAssemblyJson):
   
    def setUp(self):
        benchmark_json = "yeast/benchmark/asm_stats.json"
        result_json = "yeast/2-asm-falcon/asm_stats.json"
        self.benchmark = load_results(benchmark_json)
        self.result = load_results(result_json)

class TestYeastPreassembly(test_preassembly.TestPreassemblyJson):
   
    def setUp(self):
        benchmark_json = "yeast/benchmark/pre_assembly_stats.json"
        result_json = "yeast/0-rawreads/report/pre_assembly_stats.json"
        self.benchmark = load_results(benchmark_json)
        self.result = load_results(result_json)

if __name__ == "__main__":
    unittest.main()
