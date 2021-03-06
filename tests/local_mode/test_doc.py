import syft as sy
import torch
import syfertext

hook = sy.TorchHook(torch)
me = hook.local_worker

nlp = syfertext.load("en_core_web_lg", owner=me)


def test_add_custom_attr_doc():
    """Test adding custom attribute to Doc objects"""

    doc = nlp("Joey doesnt share food")

    # add new custom attribute
    doc.set_attribute(name="my_custom_tag", value="tag")

    # check custom attribute has been added
    assert hasattr(doc._, "my_custom_tag") and doc._.my_custom_tag == "tag"


def test_update_custom_attr_doc():
    """Test updating custom attribute of Doc objects"""

    doc = nlp("Joey doesnt share food")

    # add new custom attribute
    doc.set_attribute(name="my_custom_tag", value="tag")

    # check custom attribute has been added
    assert hasattr(doc._, "my_custom_tag") and doc._.my_custom_tag == "tag"

    # now update the attribute
    doc.set_attribute(name="my_custom_tag", value="new_tag")

    # now check the updated attribute
    assert hasattr(doc._, "my_custom_tag") and doc._.my_custom_tag == "new_tag"
