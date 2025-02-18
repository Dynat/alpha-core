from network.packet.PacketReader import *
from game.world.managers.objects.player.guild.GuildManager import GuildManager
from utils.constants.ObjectCodes import GuildCommandResults, GuildTypeCommand
from game.world.WorldSessionStateHandler import WorldSessionStateHandler


class GuildPromoteHandler(object):

    @staticmethod
    def handle(world_session, socket, reader):
        target_name = PacketReader.read_string(reader.data, 0).strip()
        target_player_mgr = WorldSessionStateHandler.find_player_by_name(target_name)
        player_mgr = world_session.player_mgr

        if not player_mgr.guild_manager:
            GuildManager.send_guild_command_result(player_mgr, GuildTypeCommand.GUILD_INVITE_S, '',
                                                   GuildCommandResults.GUILD_PLAYER_NOT_IN_GUILD)
        # TODO I guess not only GM should be able to promote?
        elif player_mgr != player_mgr.guild_manager.guild_master:
            GuildManager.send_guild_command_result(player_mgr, GuildTypeCommand.GUILD_INVITE_S, '',
                                                   GuildCommandResults.GUILD_PERMISSIONS)
        elif not target_player_mgr:
            GuildManager.send_guild_command_result(player_mgr, GuildTypeCommand.GUILD_INVITE_S, target_name,
                                                   GuildCommandResults.GUILD_PLAYER_NOT_FOUND)
        elif not player_mgr.guild_manager.is_member(target_player_mgr):
            GuildManager.send_guild_command_result(player_mgr, GuildTypeCommand.GUILD_INVITE_S, target_name,
                                                   GuildCommandResults.GUILD_PLAYER_NOT_IN_GUILD)
        elif not player_mgr.guild_manager.promote_rank(target_player_mgr):
            GuildManager.send_guild_command_result(player_mgr, GuildTypeCommand.GUILD_INVITE_S, '',
                                                   GuildCommandResults.GUILD_INTERNAL)

        return 0
