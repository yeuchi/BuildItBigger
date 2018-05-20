"""Generated message classes for apikeys version v1.

Manages the API keys associated with developer projects.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'apikeys'


class AndroidApplication(_messages.Message):
  r"""Identifier of an Android application for API key use.

  Fields:
    packageName: The package name of the application.
    sha1Fingerprint: The 20 byte SHA1 fingerprint of the application.
  """

  packageName = _messages.StringField(1)
  sha1Fingerprint = _messages.BytesField(2)


class AndroidKeyDetails(_messages.Message):
  r"""Key details that are specific to android keys.

  Fields:
    allowedApplications: A list of Android applications that are allowed to
      make API calls with this key.
  """

  allowedApplications = _messages.MessageField('AndroidApplication', 1, repeated=True)


class ApiKey(_messages.Message):
  r"""The representation of an API key managed by the `ApiKeys` API. An API
  key is used for programmatic access to a project by a service account.

  Fields:
    androidKeyDetails: Key details that are specific to android keys.
    apiTargetKeyDetails: API Target key details. These restrict which API a
      key can be used on.
    browserKeyDetails: Key details that are specific to browser keys.
    createTime: A timestamp identifying the time this API key was originally
      created. @OutputOnly
    createdBy: Email address of the user who originally created this API key.
      @OutputOnly
    currentKey: An encrypted and signed value held by this API key.
      @OutputOnly
    displayName: Human-readable display name of this API key. Modifiable by
      user.
    iosKeyDetails: Key details that are specific to iOS keys.
    keyId: Unique identifier for this ApiKey assigned by the server.
      @OutputOnly
    previousKey: The value of `current_key` before this API key was
      regenerated. @OutputOnly
    previousKeyExpireTime: The expiration time for the validity of a
      `previous_key` value after an API key regeneration. @OutputOnly
    serverKeyDetails: Key details that are specific to server keys.
  """

  androidKeyDetails = _messages.MessageField('AndroidKeyDetails', 1)
  apiTargetKeyDetails = _messages.MessageField('ApiTargetKeyDetails', 2)
  browserKeyDetails = _messages.MessageField('BrowserKeyDetails', 3)
  createTime = _messages.StringField(4)
  createdBy = _messages.StringField(5)
  currentKey = _messages.StringField(6)
  displayName = _messages.StringField(7)
  iosKeyDetails = _messages.MessageField('IosKeyDetails', 8)
  keyId = _messages.StringField(9)
  previousKey = _messages.StringField(10)
  previousKeyExpireTime = _messages.StringField(11)
  serverKeyDetails = _messages.MessageField('ServerKeyDetails', 12)


class ApiTarget(_messages.Message):
  r"""A restriction for a specific service and optionally one or multiple
  specific methods. Both fields are not case sensitive.

  Fields:
    methods: An optional list of one or more methods that can be called. If
      empty, all methods for the service are allowed. A wildcard (*) can be
      used as the last symbol. Examples:
      google.api.apikeys.v1.ApiKeys.ListApiKeys
      google.api.apikeys.v1.ApiKeys.Get* google.api.apikeys.v1.ApiKeys.Delete*
  """

  methods = _messages.StringField(1, repeated=True)


class ApiTargetKeyDetails(_messages.Message):
  r"""Key details that specify which APIs a key is allowed to be used on.

  Messages:
    ApiTargetsValue: A restriction for a specific service and optionally one
      or multiple specific methods. Requests will be allowed if they match any
      of these restrictions. If no restrictions are specified, all targets are
      allowed. Key is the service name for this restriction. It should be
      api_v1_name of service config for legacy services. For new service, it
      should be the fully qualified service name (eg. apikeys.googleapi.com).

  Fields:
    apiTargets: A restriction for a specific service and optionally one or
      multiple specific methods. Requests will be allowed if they match any of
      these restrictions. If no restrictions are specified, all targets are
      allowed. Key is the service name for this restriction. It should be
      api_v1_name of service config for legacy services. For new service, it
      should be the fully qualified service name (eg. apikeys.googleapi.com).
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ApiTargetsValue(_messages.Message):
    r"""A restriction for a specific service and optionally one or multiple
    specific methods. Requests will be allowed if they match any of these
    restrictions. If no restrictions are specified, all targets are allowed.
    Key is the service name for this restriction. It should be api_v1_name of
    service config for legacy services. For new service, it should be the
    fully qualified service name (eg. apikeys.googleapi.com).

    Messages:
      AdditionalProperty: An additional property for a ApiTargetsValue object.

    Fields:
      additionalProperties: Additional properties of type ApiTargetsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ApiTargetsValue object.

      Fields:
        key: Name of the additional property.
        value: A ApiTarget attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('ApiTarget', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  apiTargets = _messages.MessageField('ApiTargetsValue', 1)


class ApikeysProjectsApiKeysBatchDeleteRequest(_messages.Message):
  r"""A ApikeysProjectsApiKeysBatchDeleteRequest object.

  Fields:
    keyIds: The identifiers for the keys to be deleted.
    projectId: The project that owns the API keys.
  """

  keyIds = _messages.StringField(1, repeated=True)
  projectId = _messages.StringField(2, required=True)


class ApikeysProjectsApiKeysCreateRequest(_messages.Message):
  r"""A ApikeysProjectsApiKeysCreateRequest object.

  Fields:
    apiKey: A ApiKey resource to be passed as the request body.
    projectId: The project for which this API key will be created.
  """

  apiKey = _messages.MessageField('ApiKey', 1)
  projectId = _messages.StringField(2, required=True)


class ApikeysProjectsApiKeysDeleteRequest(_messages.Message):
  r"""A ApikeysProjectsApiKeysDeleteRequest object.

  Fields:
    keyId: The identifier for the key to be deleted.
    projectId: The project that owns the API key.
  """

  keyId = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)


class ApikeysProjectsApiKeysGetRequest(_messages.Message):
  r"""A ApikeysProjectsApiKeysGetRequest object.

  Fields:
    keyId: The identifier for the key to be retrieved.
    projectId: The project that owns the API key.
  """

  keyId = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)


class ApikeysProjectsApiKeysListRequest(_messages.Message):
  r"""A ApikeysProjectsApiKeysListRequest object.

  Fields:
    pageSize: Specifies the maximum number of results to be returned at a
      time.
    pageToken: Requests a specific page of results.
    projectId: Lists all API keys associated with this project.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  projectId = _messages.StringField(3, required=True)


class ApikeysProjectsApiKeysPatchRequest(_messages.Message):
  r"""A ApikeysProjectsApiKeysPatchRequest object.

  Fields:
    apiKey: A ApiKey resource to be passed as the request body.
    keyId: The identifier for the key to be modified.
    projectId: The project that owns the API key.
    updateMask: Field mask for updates.
  """

  apiKey = _messages.MessageField('ApiKey', 1)
  keyId = _messages.StringField(2, required=True)
  projectId = _messages.StringField(3, required=True)
  updateMask = _messages.StringField(4)


class ApikeysProjectsApiKeysRegenerateRequest(_messages.Message):
  r"""A ApikeysProjectsApiKeysRegenerateRequest object.

  Fields:
    keyId: The identifier for the key to be regenerated.
    projectId: The project that owns the API key.
  """

  keyId = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)


class ApikeysProjectsApiKeysRevertRequest(_messages.Message):
  r"""A ApikeysProjectsApiKeysRevertRequest object.

  Fields:
    keyId: The identifier for the key to be reverted.
    projectId: The project that owns the API key.
  """

  keyId = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)


class ApikeysProjectsDeletedApiKeysListRequest(_messages.Message):
  r"""A ApikeysProjectsDeletedApiKeysListRequest object.

  Fields:
    pageSize: Specifies the maximum number of results to be returned at a
      time.
    pageToken: Requests a specific page of results.
    projectId: Lists all deleted API keys associated with this project.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  projectId = _messages.StringField(3, required=True)


class ApikeysProjectsGetProjectForApiKeyRequest(_messages.Message):
  r"""A ApikeysProjectsGetProjectForApiKeyRequest object.

  Fields:
    apiKey: Finds the project that owns the key with this `current_key` value.
  """

  apiKey = _messages.StringField(1)


class BrowserKeyDetails(_messages.Message):
  r"""Key details that are specific to browser keys.

  Fields:
    allowedReferrers: A list of regular expressions for the referrer URLs that
      are allowed when making an API call with this key.
  """

  allowedReferrers = _messages.StringField(1, repeated=True)


class DeletedApiKey(_messages.Message):
  r"""Information about a deleted API key.

  Enums:
    SourceValueValuesEnum: What caused the key to be deleted @OutputOnly

  Fields:
    apiKey: The API key that was deleted @OutputOnly
    deletionTime: The time at which the key was deleted @OutputOnly
    source: What caused the key to be deleted @OutputOnly
  """

  class SourceValueValuesEnum(_messages.Enum):
    r"""What caused the key to be deleted @OutputOnly

    Values:
      DELETION: This API Key was deleted via a DeleteApiKey API call.
      REGENERATION: This API Key was deleted by a RegenerateApiKey API call.
    """
    DELETION = 0
    REGENERATION = 1

  apiKey = _messages.MessageField('ApiKey', 1)
  deletionTime = _messages.StringField(2)
  source = _messages.EnumField('SourceValueValuesEnum', 3)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class GetProjectForApiKeyResponse(_messages.Message):
  r"""Response message for `GetProjectForApiKey` method.

  Fields:
    projectNumber: The project number corresponding to the project key in the
      requests. The project number that owns the API key specified in the
      request.
  """

  projectNumber = _messages.IntegerField(1)


class IosKeyDetails(_messages.Message):
  r"""Key details that are specific to iOS keys.

  Fields:
    allowedBundleIds: A list of bundle IDs that are allowed when making API
      calls with this key.
  """

  allowedBundleIds = _messages.StringField(1, repeated=True)


class ListApiKeysResponse(_messages.Message):
  r"""Response message for `ListApiKeys` method.

  Fields:
    keys: A list of API keys.
    nextPageToken: The pagination token for the next page of results.
  """

  keys = _messages.MessageField('ApiKey', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListDeletedApiKeysResponse(_messages.Message):
  r"""Response message for `ListDeletedApiKeys` method.

  Fields:
    keys: A list of deleted API keys.
    nextPageToken: The pagination token for the next page of results.
  """

  keys = _messages.MessageField('DeletedApiKey', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ServerKeyDetails(_messages.Message):
  r"""Key details that are specific to server keys.

  Fields:
    allowedIps: A list of the caller IP addresses that are allowed when making
      an API call with this key.
  """

  allowedIps = _messages.StringField(1, repeated=True)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
