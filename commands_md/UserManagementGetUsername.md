# UserManagementGetUsername

## Declaration

```ats
function UserManagementGetUsername(): string;
```

## Call pattern

```ats
UserManagementGetUsername();
```

## Description

Returns the name of the current user.

## Metadata

- Category: User Management
- Code: 269569
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
if (UserManagementGetEnabled())
begin
   UserName = UserManagementGetUsername();
   FullUserName = UserManagementGetFullUsername();
   UserGroupName = UserManagementGetUserGroupName();
   IsAdmin = UserManagementUserIsAdmin();
   UIWriteNormal(StrAdd('Username: ', UserName));
   UIWriteNormal(StrAdd('Full username: ', FullUserName));
   UIWriteNormal(StrAdd('Usergroup: ', UserGroupName));
   if (IsAdmin)
   begin
      UIWriteNormal('Administrator');
   end;
end
else
begin
   UIWriteNormal('Usermanagement disabled');
end;
```

## See also

`UserManagementGetEnabled`, `UserManagementGetFullUsername`, `UserManagementGetUserGroupName`, `UserManagementLogoutUser`, `UserManagementUserIsAdmin`
