# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\tbasicswap\"\xc0\x04\n\x0cOfferMessage\x12\x18\n\x10protocol_version\x18\x01 \x01(\r\x12\x11\n\tcoin_from\x18\x02 \x01(\r\x12\x0f\n\x07\x63oin_to\x18\x03 \x01(\r\x12\x13\n\x0b\x61mount_from\x18\x04 \x01(\x04\x12\x11\n\tamount_to\x18\x05 \x01(\x04\x12\x16\n\x0emin_bid_amount\x18\x06 \x01(\x04\x12\x12\n\ntime_valid\x18\x07 \x01(\x04\x12\x33\n\tlock_type\x18\x08 \x01(\x0e\x32 .basicswap.OfferMessage.LockType\x12\x12\n\nlock_value\x18\t \x01(\r\x12\x11\n\tswap_type\x18\n \x01(\r\x12\x15\n\rproof_address\x18\x0b \x01(\t\x12\x17\n\x0fproof_signature\x18\x0c \x01(\t\x12\x15\n\rpkhash_seller\x18\r \x01(\x0c\x12\x13\n\x0bsecret_hash\x18\x0e \x01(\x0c\x12\x15\n\rfee_rate_from\x18\x0f \x01(\x04\x12\x13\n\x0b\x66\x65\x65_rate_to\x18\x10 \x01(\x04\x12\x19\n\x11\x61mount_negotiable\x18\x11 \x01(\x08\x12\x17\n\x0frate_negotiable\x18\x12 \x01(\x08\x12\x13\n\x0bproof_utxos\x18\x13 \x01(\x0c\"q\n\x08LockType\x12\x0b\n\x07NOT_SET\x10\x00\x12\x18\n\x14SEQUENCE_LOCK_BLOCKS\x10\x01\x12\x16\n\x12SEQUENCE_LOCK_TIME\x10\x02\x12\x13\n\x0f\x41\x42S_LOCK_BLOCKS\x10\x03\x12\x11\n\rABS_LOCK_TIME\x10\x04\"\xce\x01\n\nBidMessage\x12\x18\n\x10protocol_version\x18\x01 \x01(\r\x12\x14\n\x0coffer_msg_id\x18\x02 \x01(\x0c\x12\x12\n\ntime_valid\x18\x03 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\x12\x11\n\tamount_to\x18\x05 \x01(\x04\x12\x14\n\x0cpkhash_buyer\x18\x06 \x01(\x0c\x12\x15\n\rproof_address\x18\x07 \x01(\t\x12\x17\n\x0fproof_signature\x18\x08 \x01(\t\x12\x13\n\x0bproof_utxos\x18\t \x01(\x0c\"s\n\x0f\x42idMessage_test\x12\x18\n\x10protocol_version\x18\x01 \x01(\r\x12\x14\n\x0coffer_msg_id\x18\x02 \x01(\x0c\x12\x12\n\ntime_valid\x18\x03 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\x12\x0c\n\x04rate\x18\x05 \x01(\x04\"V\n\x10\x42idAcceptMessage\x12\x12\n\nbid_msg_id\x18\x01 \x01(\x0c\x12\x15\n\rinitiate_txid\x18\x02 \x01(\x0c\x12\x17\n\x0f\x63ontract_script\x18\x03 \x01(\x0c\"=\n\x12OfferRevokeMessage\x12\x14\n\x0coffer_msg_id\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\";\n\x10\x42idRejectMessage\x12\x12\n\nbid_msg_id\x18\x01 \x01(\x0c\x12\x13\n\x0breject_code\x18\x02 \x01(\r\"\xb7\x01\n\rXmrBidMessage\x12\x18\n\x10protocol_version\x18\x01 \x01(\r\x12\x14\n\x0coffer_msg_id\x18\x02 \x01(\x0c\x12\x12\n\ntime_valid\x18\x03 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\x12\x11\n\tamount_to\x18\x05 \x01(\x04\x12\x0c\n\x04pkaf\x18\x06 \x01(\x0c\x12\x0c\n\x04kbvf\x18\x07 \x01(\x0c\x12\x12\n\nkbsf_dleag\x18\x08 \x01(\x0c\x12\x0f\n\x07\x64\x65st_af\x18\t \x01(\x0c\"T\n\x0fXmrSplitMessage\x12\x0e\n\x06msg_id\x18\x01 \x01(\x0c\x12\x10\n\x08msg_type\x18\x02 \x01(\r\x12\x10\n\x08sequence\x18\x03 \x01(\r\x12\r\n\x05\x64leag\x18\x04 \x01(\x0c\"\x80\x02\n\x13XmrBidAcceptMessage\x12\x12\n\nbid_msg_id\x18\x01 \x01(\x0c\x12\x0c\n\x04pkal\x18\x02 \x01(\x0c\x12\x0c\n\x04kbvl\x18\x03 \x01(\x0c\x12\x12\n\nkbsl_dleag\x18\x04 \x01(\x0c\x12\x11\n\ta_lock_tx\x18\x05 \x01(\x0c\x12\x18\n\x10\x61_lock_tx_script\x18\x06 \x01(\x0c\x12\x18\n\x10\x61_lock_refund_tx\x18\x07 \x01(\x0c\x12\x1f\n\x17\x61_lock_refund_tx_script\x18\x08 \x01(\x0c\x12\x1e\n\x16\x61_lock_refund_spend_tx\x18\t \x01(\x0c\x12\x1d\n\x15\x61l_lock_refund_tx_sig\x18\n \x01(\x0c\"r\n\x17XmrBidLockTxSigsMessage\x12\x12\n\nbid_msg_id\x18\x01 \x01(\x0c\x12$\n\x1c\x61\x66_lock_refund_spend_tx_esig\x18\x02 \x01(\x0c\x12\x1d\n\x15\x61\x66_lock_refund_tx_sig\x18\x03 \x01(\x0c\"X\n\x18XmrBidLockSpendTxMessage\x12\x12\n\nbid_msg_id\x18\x01 \x01(\x0c\x12\x17\n\x0f\x61_lock_spend_tx\x18\x02 \x01(\x0c\x12\x0f\n\x07kal_sig\x18\x03 \x01(\x0c\"M\n\x18XmrBidLockReleaseMessage\x12\x12\n\nbid_msg_id\x18\x01 \x01(\x0c\x12\x1d\n\x15\x61l_lock_spend_tx_esig\x18\x02 \x01(\x0c\"\x81\x01\n\x13\x41\x44SBidIntentMessage\x12\x18\n\x10protocol_version\x18\x01 \x01(\r\x12\x14\n\x0coffer_msg_id\x18\x02 \x01(\x0c\x12\x12\n\ntime_valid\x18\x03 \x01(\x04\x12\x13\n\x0b\x61mount_from\x18\x04 \x01(\x04\x12\x11\n\tamount_to\x18\x05 \x01(\x04\"p\n\x19\x41\x44SBidIntentAcceptMessage\x12\x12\n\nbid_msg_id\x18\x01 \x01(\x0c\x12\x0c\n\x04pkaf\x18\x02 \x01(\x0c\x12\x0c\n\x04kbvf\x18\x03 \x01(\x0c\x12\x12\n\nkbsf_dleag\x18\x04 \x01(\x0c\x12\x0f\n\x07\x64\x65st_af\x18\x05 \x01(\x0c\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_OFFERMESSAGE']._serialized_start=30
  _globals['_OFFERMESSAGE']._serialized_end=606
  _globals['_OFFERMESSAGE_LOCKTYPE']._serialized_start=493
  _globals['_OFFERMESSAGE_LOCKTYPE']._serialized_end=606
  _globals['_BIDMESSAGE']._serialized_start=609
  _globals['_BIDMESSAGE']._serialized_end=815
  _globals['_BIDMESSAGE_TEST']._serialized_start=817
  _globals['_BIDMESSAGE_TEST']._serialized_end=932
  _globals['_BIDACCEPTMESSAGE']._serialized_start=934
  _globals['_BIDACCEPTMESSAGE']._serialized_end=1020
  _globals['_OFFERREVOKEMESSAGE']._serialized_start=1022
  _globals['_OFFERREVOKEMESSAGE']._serialized_end=1083
  _globals['_BIDREJECTMESSAGE']._serialized_start=1085
  _globals['_BIDREJECTMESSAGE']._serialized_end=1144
  _globals['_XMRBIDMESSAGE']._serialized_start=1147
  _globals['_XMRBIDMESSAGE']._serialized_end=1330
  _globals['_XMRSPLITMESSAGE']._serialized_start=1332
  _globals['_XMRSPLITMESSAGE']._serialized_end=1416
  _globals['_XMRBIDACCEPTMESSAGE']._serialized_start=1419
  _globals['_XMRBIDACCEPTMESSAGE']._serialized_end=1675
  _globals['_XMRBIDLOCKTXSIGSMESSAGE']._serialized_start=1677
  _globals['_XMRBIDLOCKTXSIGSMESSAGE']._serialized_end=1791
  _globals['_XMRBIDLOCKSPENDTXMESSAGE']._serialized_start=1793
  _globals['_XMRBIDLOCKSPENDTXMESSAGE']._serialized_end=1881
  _globals['_XMRBIDLOCKRELEASEMESSAGE']._serialized_start=1883
  _globals['_XMRBIDLOCKRELEASEMESSAGE']._serialized_end=1960
  _globals['_ADSBIDINTENTMESSAGE']._serialized_start=1963
  _globals['_ADSBIDINTENTMESSAGE']._serialized_end=2092
  _globals['_ADSBIDINTENTACCEPTMESSAGE']._serialized_start=2094
  _globals['_ADSBIDINTENTACCEPTMESSAGE']._serialized_end=2206
# @@protoc_insertion_point(module_scope)
