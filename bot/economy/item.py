import os
from pathlib import PurePosixPath

from aiohttp import ClientSession

from bot.models.profile_item import ProfileItem


class Item():
    
    def build_profile_item(self, **args) -> ProfileItem:
        """
        Builds a profile item with given parameters

        :return: Profile item
        :rtype: ProfileItem
        """
        return ProfileItem(**args)

    async def save_profile_item(self, profile_item: ProfileItem, url: str):
        """
        Saves given profile item with given image

        :param profile_item: Profile item to be persisted
        :type profile_item: ProfileItem
        :param file_contents: Image's URL
        :type file_contents: url
        :return: Created profile item's id
        :rtype: str
        """
        default_path = os.path.join(os.getcwd(), 'bot', 'images', 'profile_items')
        directory_path = os.path.join(
            os.environ.get("PROFILE_ITEM_IMAGES_PATH", default_path), f'{str(profile_item.type)}s'
        )
        os.makedirs(directory_path, exist_ok=True)

        filename = PurePosixPath(url).parts[-1]
        async with ClientSession() as session:
            async with session.get(url) as response:
                file_contents = await response.read()

        profile_item.file_path = os.path.join(directory_path, filename)
        with open(profile_item.file_path, 'wb') as f:
            f.write(file_contents)
        
        return await ProfileItem.save(profile_item)
