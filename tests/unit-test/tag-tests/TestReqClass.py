#
# Requirement Management Toolset
#
# Unit test for ReqClass
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqClass import ReqClass
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException

class TestReqClass:

    def test_positive_01(self):
        "Requirement Tag Class - no Class given"
        opts = {}
        config = {}
        req = {}

        rt = ReqClass(opts, config)
        name, value = rt.rewrite("Class-test", req)
        assert(name=="Class")
        assert(value==Requirement.ct_detailable)

    def test_positive_02(self):
        "Requirement Tag Class - no Class detailable"
        opts = {}
        config = {}
        req = {"Class": "detailable"}

        rt = ReqClass(opts, config)
        name, value = rt.rewrite("Class-test", req)
        assert(name=="Class")
        assert(value==Requirement.ct_detailable)

    def test_positive_03(self):
        "Requirement Tag Class - no Class implementable"
        opts = {}
        config = {}
        req = {"Class": "implementable"}

        rt = ReqClass(opts, config)
        name, value = rt.rewrite("Class-test", req)
        assert(name=="Class")
        assert(value==Requirement.ct_implementable)

    def test_negative_01(self):
        "Requirement Tag Class - unsupported Class value"
        opts = {}
        config = {}
        req = {"Class": "something_completly_different"}

        rt = ReqClass(opts, config)
        try:
            name, value = rt.rewrite("Class-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.eid==1)
