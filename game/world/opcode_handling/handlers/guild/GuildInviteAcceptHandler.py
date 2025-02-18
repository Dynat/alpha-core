from game.world.managers.objects.player.guild.GuildManager import GuildManager
from utils.constants.ObjectCodes import GuildCommandResults, GuildTypeCommand


class GuildInviteAcceptHandler(object):

    @staticmethod
    def handle(world_session, socket, reader):
        player_mgr = world_session.player_mgr

        if player_mgr.guid in GuildManager.PENDING_INVITES:
            inviter = GuildManager.PENDING_INVITES[player_mgr.guid].inviter
            GuildManager.PENDING_INVITES.pop(player_mgr.guid)
            inviter.guild_manager.add_new_member(player_mgr)
        else:
            GuildManager.send_guild_command_result(player_mgr, GuildTypeCommand.GUILD_INVITE_S, '',
                                                   GuildCommandResults.GUILD_INTERNAL)

        return 0
